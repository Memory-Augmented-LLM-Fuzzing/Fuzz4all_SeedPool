"""Rare edge detection for coverage data."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RareEdge:
    """Represents a rarely-executed line of code."""
    file: str
    line: int
    execution_count: int
    is_new: bool = False

    def __str__(self) -> str:
        return f"{self.file}:{self.line} (executed {self.execution_count}x)"

    def to_id_string(self) -> str:
        """Convert to compact ID format."""
        return f"{self.file}:{self.line}"


class EdgeDetector:
    """Detects rare edges from coverage data."""

    def __init__(self, threshold: int = 3):
        """
        Initialize edge detector.

        Args:
            threshold: Execution count threshold for rare edges
                      (edges with <threshold executions are considered rare)
        """
        self.threshold = threshold

    def detect_rare_edges(
        self,
        current_coverage: Dict[str, Dict[int, int]],
        historical_aggregate: Dict[str, Dict[int, int]],
    ) -> List[RareEdge]:
        """
        Detect rarely-executed edges.

        Args:
            current_coverage: {filename: {line: count}} from current test
            historical_aggregate: {filename: {line: cumulative_count}} from history

        Returns:
            List of RareEdge objects for lines with <threshold total executions
        """
        rare_edges = []

        for filename, line_counts in current_coverage.items():
            if filename not in historical_aggregate:
                historical_aggregate[filename] = {}

            file_history = historical_aggregate[filename]

            for line_num, current_count in line_counts.items():
                # Get total execution count (current + historical)
                historical_count = file_history.get(line_num, 0)
                total_count = current_count + historical_count

                # Only consider lines that were actually executed
                if current_count > 0 and total_count < self.threshold:
                    is_new = line_num not in file_history
                    rare_edges.append(
                        RareEdge(
                            file=filename,
                            line=line_num,
                            execution_count=total_count,
                            is_new=is_new,
                        )
                    )

        return rare_edges

    def get_edge_summary(self, rare_edges: List[RareEdge]) -> Dict[str, int]:
        """Get summary of rare edges by file."""
        summary = {}
        for edge in rare_edges:
            summary[edge.file] = summary.get(edge.file, 0) + 1
        return summary
