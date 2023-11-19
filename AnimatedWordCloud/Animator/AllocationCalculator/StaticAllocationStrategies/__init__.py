from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.MagneticAllocation import (
    allocate_magnetic,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.Word import (
    Word,
)

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.Rect import (
    Rect,
    is_point_hitting_rect,
    is_point_hitting_rects,
)

__all__ = [
    "allocate_magnetic",
    "Word",
    "Rect",
    "is_point_hitting_rect",
    "is_point_hitting_rects",
]
