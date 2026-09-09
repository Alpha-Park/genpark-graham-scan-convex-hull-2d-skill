"""MCP Server for Convex Hull 2D Skill."""
import json
import sys
from client import ConvexHull2D

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "compute_convex_hull",
                            "description": "Calculate 2D Convex Hull, enclosed area, and perimeter",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "points": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    }
                                },
                                "required": ["points"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                pts = [tuple(p) for p in args["points"]]
                hull = ConvexHull2D.compute_hull(pts)
                out = {
                    "convex_hull": hull,
                    "vertex_count": len(hull),
                    "area": ConvexHull2D.polygon_area(hull),
                    "perimeter": ConvexHull2D.polygon_perimeter(hull)
                }
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
