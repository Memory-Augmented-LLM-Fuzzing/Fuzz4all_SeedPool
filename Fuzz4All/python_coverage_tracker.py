"""Python code coverage tracking using coverage.py library."""

import os
import tempfile
from typing import Dict, List, Optional


class PythonCoverageTracker:
    """Track code coverage for Python SUTs using coverage.py."""

    def __init__(self, target_files: List[str]):
        """
        Initialize coverage tracker.

        Args:
            target_files: List of Python file paths to measure coverage for (the SUTs)
        """
        self.target_files = target_files
        self.coverage = None
        self.current_data = None
        self.temp_dir = None
        self._initialize_coverage()

    def _initialize_coverage(self) -> None:
        """Initialize coverage.py with branch coverage enabled."""
        try:
            import coverage
            self.coverage = coverage
        except ImportError:
            raise ImportError(
                "coverage library not found. Install with: pip install coverage>=7.0"
            )

    def start_coverage(self) -> None:
        """Start collecting coverage for a test."""
        try:
            import coverage as cov_module

            # Create temp directory for coverage files
            self.temp_dir = tempfile.mkdtemp()
            coverage_file = os.path.join(self.temp_dir, ".coverage")

            # Start coverage with branch coverage enabled
            # source parameter specifies which files to measure
            self.coverage_obj = cov_module.Coverage(
                data_file=coverage_file,
                branch=True,
                source=self.target_files,
                omit=["<string>", "*/__pycache__/*"]
            )
            self.coverage_obj.start()
        except Exception as e:
            raise RuntimeError(f"Failed to start coverage: {e}")

    def stop_coverage(self) -> Dict[str, Dict[int, int]]:
        """
        Stop collecting coverage and extract execution counts.

        Returns:
            Dict mapping {filename: {line_number: execution_count}}
        """
        try:
            if self.coverage_obj is None:
                return {}

            self.coverage_obj.stop()
            self.coverage_obj.save()

            # Extract line execution counts
            coverage_data = self._extract_line_counts()

            self.cleanup()

            return coverage_data
        except Exception as e:
            print(f"Error stopping coverage: {e}")
            return {}

    def _extract_line_counts(self) -> Dict[str, Dict[int, int]]:
        """
        Extract line execution counts from coverage data.

        Returns:
            Dict: {filename: {line_number: execution_count}}
        """
        try:
            result = {}

            for target_file in self.target_files:
                if not os.path.exists(target_file):
                    continue

                file_coverage = {}

                try:
                    # Try to get coverage data
                    data = self.coverage_obj.get_data()
                    executed_lines = set()

                    # Handle different coverage.py APIs
                    if hasattr(data, 'lines') and callable(data.lines):
                        # Newer API: lines() is a method
                        try:
                            executed_lines = set(data.lines(target_file))
                        except:
                            pass
                    elif hasattr(data, 'lines'):
                        # Older API: lines is a dict-like
                        try:
                            executed_lines = set(data.lines.get(target_file, []))
                        except:
                            pass

                    # Count total lines in file
                    with open(target_file, 'r') as f:
                        total_lines = len(f.readlines())

                    # Create line count dict
                    for line_num in range(1, total_lines + 1):
                        file_coverage[line_num] = 1 if line_num in executed_lines else 0

                except Exception as e:
                    # Fallback: return file structure even if no coverage
                    try:
                        with open(target_file, 'r') as f:
                            total_lines = len(f.readlines())
                        file_coverage = {i: 0 for i in range(1, total_lines + 1)}
                    except:
                        pass

                if file_coverage:
                    result[target_file] = file_coverage

            return result
        except Exception as e:
            print(f"Error extracting line counts: {e}")
            return {}

    def get_coverage_percentage(self, coverage_data: Dict[str, Dict[int, int]]) -> float:
        """
        Calculate total coverage percentage.

        Args:
            coverage_data: Coverage dict from stop_coverage()

        Returns:
            Coverage percentage (0-100)
        """
        total_lines = 0
        executed_lines = 0

        for file_coverage in coverage_data.values():
            total_lines += len(file_coverage)
            executed_lines += sum(1 for count in file_coverage.values() if count > 0)

        if total_lines == 0:
            return 0.0

        return (executed_lines / total_lines) * 100.0

    def cleanup(self) -> None:
        """Remove temporary coverage files."""
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                import shutil
                shutil.rmtree(self.temp_dir)
            except:
                pass
