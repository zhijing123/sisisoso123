---
name: weather-query
description: A skill for querying current weather information. Use this skill when the user wants to know the current weather or any weather-related queries for a specific location.
---

# Weather Query

## Overview

This skill enables querying current weather information for cities using multiple weather APIs with automatic fallback. It concurrently queries two weather services and returns the first successful response, ensuring high availability.

## When to Use This Skill

Trigger this skill when the user asks about weather, such as:
- "What's the weather like in Shanghai?"
- "查询北京天气"
- "今天天气怎么样？"
- "Is it raining in Tokyo right now?"
- Any query about current weather conditions for a city

## Quick Start

### Prerequisites

1. **Install Dependencies**:
   ```bash
   pip install requests
   ```

### Basic Usage

```bash
# Query weather for a city
python weather_query.py "Shanghai"

# Query weather for Chinese cities
python weather_query.py "北京"
python weather_query.py "深圳"

# Query using city ID (for Meizu API)
python weather_query.py "101240101"
```

## How It Works

The script concurrently queries two weather APIs:

| API | Endpoint | Parameter |
|-----|----------|-----------|
| Custom Weather Server | `http://727cc816.katze.click/weather` | `city` |
| Meizu Weather API | `http://aider.meizu.com/app/weather/listWeather` | `cityIds` |

**Strategy**: Both APIs are called simultaneously. The first successful response is returned immediately, ensuring fast results even if one API is slow or unavailable.

## Output Example

When you run the script, you'll get output like:

```
Querying weather for: Shanghai

[Data from API 1]

<weather information from the responding API>
```

The `[Data from API X]` indicates which weather service provided the data.

## Error Handling

- If both APIs fail to respond, an error message will be displayed
- The script uses a 10-second timeout for each API call
- No API key is required for either service

## Resources

### scripts/

- **weather_query.py**: Main script for querying weather using multiple APIs with concurrent requests and automatic fallback.