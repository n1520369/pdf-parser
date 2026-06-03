from PyPDF2 import PdfReader

pdf_path = input("Enter PDF file path: ")

try:
    reader = PdfReader(pdf_path)

    print(f"\nTotal Pages: {len(reader.pages)}")

    print("\nExtracted Text:\n")

    for page in reader.pages:
        print(page.extract_text())

except Exception as e:
    print(f"Error: {e}")
