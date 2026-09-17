# App Store & Google Play Data API

> App intelligence across Google Play and the App Store: details, reviews, and search in one API.

Part of the **DataLeads** API suite (Data category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/app/gplay/details` | V1 App Gplay Details |
| POST | `/app/gplay/reviews` | V1 App Gplay Reviews |
| POST | `/app/apple/search` | V1 App Apple Search |
| POST | `/app/apple/details` | V1 App Apple Details |
| POST | `/app/apple/reviews` | V1 App Apple Reviews |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/app/gplay/details \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "appId": "com.spotify.music"}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/app-data`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/app-data-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
