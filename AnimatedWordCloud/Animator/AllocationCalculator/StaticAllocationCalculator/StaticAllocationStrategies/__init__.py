from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.StaticAllocationStrategy import (
    StaticAllocationStrategy,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.MagneticAllocation import (
    MagneticAllocation,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.RandomAllocation import (
    allocate_randomly,
)

__all__ = [
    "StaticAllocationStrategy",
    "allocate_randomly",
    "MagneticAllocation",
]
