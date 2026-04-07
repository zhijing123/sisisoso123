#!/usr/bin/env python3
"""
Bill Analysis Script
Sends bill/invoice information to a custom analysis server.

Usage:
    python bill_analysis.py <bill_content>
    python bill_analysis.py --file <file_path>
    python bill_analysis.py --file <file_path> --api <custom_api_url>

Example:
    python bill_analysis.py "账单: 餐饮 150元, 交通 50元"
    python bill_analysis.py --file my_bill.txt
"""

import sys
import requests
import argparse
from pathlib import Path
from typing import Optional

# Default API endpoint
DEFAULT_API_URL = "http://727cc816.katze.click/bill"
TIMEOUT = 30


def analyze_bill(bill_content: str, api_url: str = DEFAULT_API_URL) -> Optional[str]:
    """
    Send bill content to analysis server and return the result.
    
    Args:
        bill_content: The bill/invoice information to analyze
        api_url: The API endpoint URL
        
    Returns:
        Analysis result string or None if failed
    """
    params = {"bill": bill_content}
    
    try:
        print(f"Sending bill to analysis server...")
        print(f"API: {api_url}")
        print()
        
        response = requests.get(api_url, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        
        return response.text
        
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return f"Error: Cannot connect to analysis server at {api_url}"
    except requests.exceptions.HTTPError as e:
        return f"Error: HTTP error occurred: {e}"
    except Exception as e:
        return f"Error: {str(e)}"


def read_bill_from_file(file_path: str) -> Optional[str]:
    """
    Read bill content from a file.
    
    Args:
        file_path: Path to the file containing bill information
        
    Returns:
        File content or None if failed
    """
    try:
        path = Path(file_path)
        if not path.exists():
            print(f"Error: File not found: {file_path}")
            return None
        
        # Try different encodings
        encodings = ['utf-8', 'gbk', 'gb2312', 'latin1']
        for encoding in encodings:
            try:
                return path.read_text(encoding=encoding)
            except UnicodeDecodeError:
                continue
        
        # Fallback to binary read
        return path.read_bytes().decode('utf-8', errors='ignore')
        
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Analyze bills/invoices using a custom analysis server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "账单: 餐饮 150元"
  %(prog)s --file receipt.txt
  %(prog)s --file bill.txt --api http://custom-server.com/analyze
        """
    )
    
    # Positional argument for direct bill content
    parser.add_argument(
        'bill_content',
        nargs='?',
        help='The bill/invoice content to analyze'
    )
    
    # Option to read from file
    parser.add_argument(
        '-f', '--file',
        help='Read bill content from a file',
        metavar='FILE_PATH'
    )
    
    # Option to customize API endpoint
    parser.add_argument(
        '-a', '--api',
        help='Custom API endpoint URL',
        default=DEFAULT_API_URL,
        metavar='URL'
    )
    
    args = parser.parse_args()
    
    # Determine bill content source
    bill_content = None
    
    if args.file:
        # Read from file
        bill_content = read_bill_from_file(args.file)
        if bill_content:
            print(f"[File]: Loaded bill from {args.file}")
            print()
    elif args.bill_content:
        # Use direct content
        bill_content = args.bill_content
    else:
        # No input provided
        print(__doc__)
        print("\nError: Please provide bill content either as argument or via --file option.")
        sys.exit(1)
    
    if not bill_content or not bill_content.strip():
        print("Error: Bill content is empty.")
        sys.exit(1)
    
    # Print preview of bill content
    preview = bill_content[:200] + "..." if len(bill_content) > 200 else bill_content
    print(f"[Preview]: {preview}")
    print()
    
    # Send for analysis
    result = analyze_bill(bill_content, args.api)
    
    if result:
        print("=" * 50)
        print("[Analysis Result]")
        print("=" * 50)
        print()
        print(result)
    else:
        print("Error: Failed to get analysis result.")
        sys.exit(1)


if __name__ == "__main__":
    main()