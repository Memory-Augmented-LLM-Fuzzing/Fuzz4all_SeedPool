"""Seed pool for managing high-value fuzzing seeds."""

import json
import os
from dataclasses import asdict, dataclass
from typing import List, Optional


@dataclass
class SeedMetadata:
    """Metadata for a seed in the pool."""
    seed_id: str  # filename identifier
    seed_content: str  # actual code
    bug_type: str  # type of bug found (e.g., "compiler_error", "runtime_error")
    timestamp: float  # when seed was added
    coverage_increase: Optional[float] = None  # coverage delta if tracked
    edges_triggered: Optional[List[str]] = None  # rare edges triggered


class SeedPool:
    """Manages a pool of high-value fuzzing seeds."""

    def __init__(self, pool_dir: str):
        """
        Initialize seed pool.

        Args:
            pool_dir: Directory to store pool metadata and seeds
        """
        self.pool_dir = pool_dir
        self.metadata_file = os.path.join(pool_dir, "pool_metadata.json")
        self.seeds_dir = os.path.join(pool_dir, "seeds")
        self.seeds: List[SeedMetadata] = []

        os.makedirs(self.seeds_dir, exist_ok=True)
        self._load_pool()

    def add_seed(
        self,
        seed_id: str,
        seed_content: str,
        bug_type: str,
        timestamp: float,
        coverage_increase: Optional[float] = None,
        edges_triggered: Optional[List[str]] = None,
    ) -> None:
        """
        Add a high-value seed to the pool.

        Args:
            seed_id: Unique identifier for the seed
            seed_content: The actual code content
            bug_type: Type of bug/issue found
            timestamp: When the seed was generated
            coverage_increase: Optional coverage delta
            edges_triggered: Optional list of rare edges triggered
        """
        metadata = SeedMetadata(
            seed_id=seed_id,
            seed_content=seed_content,
            bug_type=bug_type,
            timestamp=timestamp,
            coverage_increase=coverage_increase,
            edges_triggered=edges_triggered or [],
        )
        self.seeds.append(metadata)
        self._save_seed_file(metadata)
        self._save_metadata()

    def get_random_seed(self) -> Optional[SeedMetadata]:
        """Get a random seed from the pool for mutation."""
        if not self.seeds:
            return None
        import random
        return random.choice(self.seeds)

    def get_all_seeds(self) -> List[SeedMetadata]:
        """Get all seeds in the pool."""
        return self.seeds

    def get_seeds_by_bug_type(self, bug_type: str) -> List[SeedMetadata]:
        """Get seeds filtered by bug type."""
        return [s for s in self.seeds if s.bug_type == bug_type]

    def size(self) -> int:
        """Get the number of seeds in the pool."""
        return len(self.seeds)

    def get_statistics(self) -> dict:
        """Get pool statistics."""
        if not self.seeds:
            return {
                "total_seeds": 0,
                "bug_types": {},
                "total_coverage_increase": 0,
            }

        bug_type_counts = {}
        for seed in self.seeds:
            bug_type_counts[seed.bug_type] = bug_type_counts.get(seed.bug_type, 0) + 1

        total_coverage = sum(
            s.coverage_increase for s in self.seeds if s.coverage_increase
        )

        return {
            "total_seeds": len(self.seeds),
            "bug_types": bug_type_counts,
            "total_coverage_increase": total_coverage,
        }

    def print_report(self) -> None:
        """Print seed pool statistics report."""
        stats = self.get_statistics()
        print("\n" + "=" * 60)
        print("Seed Pool Report")
        print("=" * 60)
        print(f"Total seeds: {stats['total_seeds']}")
        if stats["bug_types"]:
            print("Bug types:")
            for bug_type, count in stats["bug_types"].items():
                print(f"  - {bug_type}: {count}")
        if stats["total_coverage_increase"] > 0:
            print(f"Total coverage increase: {stats['total_coverage_increase']:.2f}%")

        # Print seeds with coverage/edge info
        has_coverage_data = any(s.coverage_increase is not None for s in self.seeds)
        has_edge_data = any(s.edges_triggered for s in self.seeds)

        if has_coverage_data or has_edge_data:
            print("\nHigh-value seeds:")
            for seed in self.seeds:
                coverage_str = (
                    f" (coverage: {seed.coverage_increase:.2f}%)"
                    if seed.coverage_increase
                    else ""
                )
                edges_str = (
                    f" (edges: {len(seed.edges_triggered)})"
                    if seed.edges_triggered
                    else ""
                )
                print(f"  - {seed.seed_id}: {seed.bug_type}{coverage_str}{edges_str}")

        print("=" * 60 + "\n")

    def _save_seed_file(self, metadata: SeedMetadata) -> None:
        """Save seed content to file."""
        seed_file = os.path.join(self.seeds_dir, f"{metadata.seed_id}.txt")
        try:
            with open(seed_file, "w", encoding="utf-8") as f:
                f.write(metadata.seed_content)
        except Exception as e:
            print(f"Error saving seed file {seed_file}: {e}")

    def _save_metadata(self) -> None:
        """Save pool metadata to JSON file."""
        try:
            metadata_list = [asdict(seed) for seed in self.seeds]
            with open(self.metadata_file, "w", encoding="utf-8") as f:
                json.dump(metadata_list, f, indent=2)
        except Exception as e:
            print(f"Error saving pool metadata: {e}")

    def _load_pool(self) -> None:
        """Load pool metadata from file."""
        if not os.path.exists(self.metadata_file):
            return

        try:
            with open(self.metadata_file, "r", encoding="utf-8") as f:
                metadata_list = json.load(f)

            for item in metadata_list:
                # Load seed content from file
                seed_file = os.path.join(self.seeds_dir, f"{item['seed_id']}.txt")
                if os.path.exists(seed_file):
                    with open(seed_file, "r", encoding="utf-8") as f:
                        item["seed_content"] = f.read()

                self.seeds.append(SeedMetadata(**item))
        except Exception as e:
            print(f"Error loading pool metadata: {e}")

    def clear(self) -> None:
        """Clear all seeds from the pool."""
        self.seeds.clear()
        self._save_metadata()
