from .StaticAllocationStrategy import (
    StaticAllocationStrategy,
)

from .MagneticAllocation import (
    MagneticAllocation,
)

from .RandomAllocation import (
    allocate_randomly,
)

from .Word import (
    Word,
)

from .Rect import (
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
]
