"""
Autonomous Agent 2D Convex Hull Skill (Graham Scan / Monotone Chain)
Pure Python Standard Library implementation in O(n log n).
"""
import math
from typing import List, Tuple, Dict, Any

class ConvexHull2D:
    """
    Monotone Chain Convex Hull algorithm in 2D.
    """
    @staticmethod
    def orientation(p: Tuple[float, float], q: Tuple[float, float], r: Tuple[float, float]) -> float:
        return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

    @staticmethod
    def compute_hull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        pts = sorted(list(set(points)))
        if len(pts) <= 2:
            return pts

        lower = []
        for p in pts:
            while len(lower) >= 2 and ConvexHull2D.orientation(lower[-2], lower[-1], p) <= 1e-9:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and ConvexHull2D.orientation(upper[-2], upper[-1], p) <= 1e-9:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    @staticmethod
    def polygon_area(hull: List[Tuple[float, float]]) -> float:
        n = len(hull)
        if n < 3:
            return 0.0
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]
        return round(abs(area) / 2.0, 4)

    @staticmethod
    def polygon_perimeter(hull: List[Tuple[float, float]]) -> float:
        n = len(hull)
        if n < 2:
            return 0.0
        perim = 0.0
        for i in range(n):
            j = (i + 1) % n
            perim += math.hypot(hull[i][0] - hull[j][0], hull[i][1] - hull[j][1])
        return round(perim, 4)
