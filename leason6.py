"""
Ubuntu Image Fetcher
====================
"A person is a person through other persons."

This program demonstrates the spirit of Ubuntu by connecting to the global web community,
fetching shared images respectfully, and organizing them for later appreciation.

Author: [Your Name]
Repository: https://github.com/YourUsername/Ubuntu_Requests
"""

import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one using a hash."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"
    return filename

def file_exists(filepath):
    """Check if a file already exists to avoid duplicates."""
    return os.path.exists(filepath)

def fetch_image(url):
    """Download an image from the given URL and save it locally."""
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Check if the content type is actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ The URL does not contain an image: {url}")
            return

        # Extract filename or create one
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Avoid duplicate downloads
        if file_exists(filepath):
            print(f"⚠ Skipped duplicate: {filename}")
            return

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.MissingSchema:
        print("✗ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.Timeout:
        print("✗ Connection timed out. Please try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user (comma-separated)
    urls = input("Please enter one or more image URLs (comma-separated): ").split(",")

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched. 🙏")

if __name__ == "__main__":
    main()
