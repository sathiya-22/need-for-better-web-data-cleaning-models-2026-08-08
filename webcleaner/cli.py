import argparse
import os
from .cleaner import WebCleaner
from .extractor import ContentExtractor

def main():
    parser = argparse.ArgumentParser(
        description="Clean and extract main content from HTML files."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="fixture_data/sample_webpage.html",
        help="Path to the input HTML file. Defaults to fixture_data/sample_webpage.html."
    )
    parser.add_argument(
        "-o", "--output_file",
        help="Optional path to save the cleaned and extracted content."
    )
    parser.add_argument(
        "-c", "--clean_only",
        action="store_true",
        help="Only perform basic cleaning, do not attempt main content extraction."
    )

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        return

    with open(args.input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    cleaner = WebCleaner()
    cleaned_text = cleaner.clean_html(html_content)

    output_content = ""
    if args.clean_only:
        output_content = cleaned_text
        print("--- Cleaned HTML (Text Only) ---")
    else:
        extractor = ContentExtractor()
        extracted_content = extractor.extract_main_content(cleaned_text)
        output_content = extracted_content
        print("--- Extracted Main Content ---")

    print(output_content)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(output_content)
        print(f"\nOutput saved to: {args.output_file}")

if __name__ == "__main__":
    main()
