"""Example usage for Convex Hull 2D Skill."""
from client import ConvexHull2D

def main():
    print("Executing Convex Hull 2D...")
    pts = [(0.0, 0.0), (1.0, 1.0), (2.0, 2.0), (0.0, 2.0), (2.0, 0.0), (1.0, 0.5)]
    hull = ConvexHull2D.compute_hull(pts)
    area = ConvexHull2D.polygon_area(hull)
    perim = ConvexHull2D.polygon_perimeter(hull)

    print(f"Convex Hull ({len(hull)} vertices):", hull)
    print(f"Area: {area}, Perimeter: {perim}")
    assert area == 4.0, f"Expected 4.0, got {area}"
    print("Convex Hull 2D verified successfully!")

if __name__ == "__main__":
    main()
