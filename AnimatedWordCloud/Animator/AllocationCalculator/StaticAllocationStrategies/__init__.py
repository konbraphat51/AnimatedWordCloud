from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.StaticAllocationStrategy import (
    StaticAllocationStrategy,
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
    "StaticAllocationStrategy",
    "allocate_magnetic",
    "Word",
    "Rect",
    "is_point_hitting_rect",
    "is_point_hitting_rects",
]
