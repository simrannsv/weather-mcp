# Weather MCP Server

A minimal [MCP](https://modelcontextprotocol.io) server that exposes a `get_weather` tool, letting any MCP-compatible LLM client (like Claude) fetch live weather for a city.

## What it does

Registers a single tool, `get_weather(city)`, that queries [wttr.in](https://wttr.in) (a free, no-API-key weather service) and returns a short current-conditions summary — e.g. temperature, sky, wind — for the given city.

## Tech

- **[FastMCP](https://github.com/modelcontextprotocol/python-sdk)** (Python MCP SDK) — handles the MCP protocol so the tool just needs to be a decorated async function
- **httpx** — async HTTP client for the weather request
- **stdio transport** — the server communicates over standard input/output, the standard way local MCP servers talk to a client

## Setup

```bash
pip install mcp httpx
```

## Run

```bash
python weather_server.py
```

To use it with Claude Desktop or another MCP client, add it to your client's MCP server config, e.g.:

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["/absolute/path/to/weather_server.py"]
    }
  }
}
```

## Example

Once connected, an LLM client can call:

```
get_weather("Hyderabad")
```

and get back something like:

```
Hyderabad: ☀️ +32°C
```

## Possible next steps

- Add a forecast tool (multi-day outlook)
- Add severe weather alerts
- Support structured (JSON) output instead of plain text, for richer client-side rendering
