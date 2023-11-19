from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.StaticAllocationStrategy import (
    StaticAllocationStrategy,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.MagneticAllocation import (
    MagneticAllocation,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.RandomAllocation import (
    allocate_randomly,
    put_randomly,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.Word import (
    Word,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.Rect import (
    Rect,
    is_point_hitting_rect,
    is_point_hitting_rects,
    is_rect_hitting_rect,
    is_rect_hitting_rects,
)

__all__ = [
    "StaticAllocationStrategy",
    "allocate_randomly",
    "Word",
    "Rect",
    "is_point_hitting_rect",
    "is_point_hitting_rects",
    "is_rect_hitting_rect",
    "is_rect_hitting_rects",
    "MagneticAllocation",
    "put_randomly",
]
