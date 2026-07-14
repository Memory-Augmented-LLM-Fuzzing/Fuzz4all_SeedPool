"""Coverage history tracking and delta calculation."""

from typing import Dict, List, Tuple
from Fuzz4All.edge_detector import EdgeDetector, RareEdge


class CoverageHistory:
    """Maintains coverage history and calculates coverage deltas."""

    def __init__(self, target_files: List[str], max_history: int = 50):
        """
        Initialize coverage history.

        Args:
            target_files: List of Python files being tracked
            max_history: Keep last N test results for delta calculation
        """
        self.target_files = target_files
        self.max_history = max_history
        self.history: List[Dict[str, Dict[int, int]]] = []
        self.aggregate: Dict[str, Dict[int, int]] = {}
        self.coverage_percentages: List[float] = []
        self.edge_detector = EdgeDetector(threshold=3)

    def add_coverage(self, coverage_data: Dict[str, Dict[int, int]]) -> None:
        """
        Record coverage from a single test.

        Args:
            coverage_data: {filename: {line: count}} from one test execution
        """
        # Add to history
        self.history.append(coverage_data)

        # Maintain max history size
        if len(self.history) > self.max_history:
            self.history.pop(0)

        # Update aggregate
        self._update_aggregate(coverage_data)

        # Calculate and store coverage percentage
        coverage_pct = self._calculate_coverage_percentage(coverage_data)
        self.coverage_percentages.append(coverage_pct)

        if len(self.coverage_percentages) > self.max_history:
            self.coverage_percentages.pop(0)

    def _update_aggregate(self, coverage_data: Dict[str, Dict[int, int]]) -> None:
        """Update cumulative coverage aggregate."""
        for filename, line_counts in coverage_data.items():
            if filename not in self.aggregate:
                self.aggregate[filename] = {}

            file_agg = self.aggregate[filename]
            for line_num, count in line_counts.items():
                if count > 0:
                    # Update to track that this line was executed
                    file_agg[line_num] = file_agg.get(line_num, 0) + 1

    def _calculate_coverage_percentage(
        self, coverage_data: Dict[str, Dict[int, int]]
    ) -> float:
        """Calculate coverage percentage for given coverage data."""
        total_lines = 0
        executed_lines = 0

        for file_coverage in coverage_data.values():
            total_lines += len(file_coverage)
            executed_lines += sum(1 for count in file_coverage.values() if count > 0)

        if total_lines == 0:
            return 0.0

        return (executed_lines / total_lines) * 100.0

    def get_coverage_delta(self, current: Dict[str, Dict[int, int]]) -> float:
        """
        Calculate coverage improvement vs. historical average.

        Returns:
            Delta in percentage points (e.g., 2.5 for +2.5% improvement)
        """
        if not self.coverage_percentages:
            # First test - any coverage is new coverage
            current_pct = self._calculate_coverage_percentage(current)
            return current_pct

        # Calculate average coverage from history
        avg_coverage = sum(self.coverage_percentages) / len(self.coverage_percentages)

        # Calculate current coverage
        current_pct = self._calculate_coverage_percentage(current)

        # Delta
        delta = current_pct - avg_coverage

        return max(0.0, delta)  # Don't report negative deltas

    def detect_rare_edges(self, current: Dict[str, Dict[int, int]]) -> List[RareEdge]:
        """
        Find lines executed <3 times across all history.

        Args:
            current: Current test coverage

        Returns:
            List of RareEdge objects
        """
        return self.edge_detector.detect_rare_edges(current, self.aggregate)

    def get_total_lines_covered(self) -> int:
        """Get total unique lines covered in aggregate."""
        total = 0
        for file_agg in self.aggregate.values():
            total += len(file_agg)
        return total

    def get_total_executable_lines(self) -> int:
        """Get total executable lines across all target files."""
        total = 0
        for target_file in self.target_files:
            try:
                with open(target_file, 'r') as f:
                    total += len(f.readlines())
            except:
                pass
        return total

    def get_statistics(self) -> Dict:
        """Get coverage statistics."""
        total_covered = self.get_total_lines_covered()
        total_executable = self.get_total_executable_lines()

        if total_executable == 0:
            coverage_pct = 0.0
        else:
            coverage_pct = (total_covered / total_executable) * 100.0

        return {
            "total_covered": total_covered,
            "total_executable": total_executable,
            "coverage_percentage": coverage_pct,
            "tests_run": len(self.history),
            "average_coverage": (
                sum(self.coverage_percentages) / len(self.coverage_percentages)
                if self.coverage_percentages
                else 0.0
            ),
        }

    def clear(self) -> None:
        """Clear history and aggregate data."""
        self.history.clear()
        self.aggregate.clear()
        self.coverage_percentages.clear()
