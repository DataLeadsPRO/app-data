import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('App Store & Google Play Data API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "app_gplay_details",
    "method": "POST",
    "path": "/app/gplay/details",
    "description": "V1 App Gplay Details"
  },
  {
    "name": "app_gplay_reviews",
    "method": "POST",
    "path": "/app/gplay/reviews",
    "description": "V1 App Gplay Reviews"
  },
  {
    "name": "app_apple_search",
    "method": "POST",
    "path": "/app/apple/search",
    "description": "V1 App Apple Search"
  },
  {
    "name": "app_apple_details",
    "method": "POST",
    "path": "/app/apple/details",
    "description": "V1 App Apple Details"
  },
  {
    "name": "app_apple_reviews",
    "method": "POST",
    "path": "/app/apple/reviews",
    "description": "V1 App Apple Reviews"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
