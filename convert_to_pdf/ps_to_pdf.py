import ghostscript
import sys

def ps_to_pdf(ps_path, pdf_path):
    args = [
        "ps2pdf",  # Arbitrary name (used by Ghostscript)
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=pdfwrite",
        f"-sOutputFile={pdf_path}",
        ps_path,
    ]

    # Convert args to bytes
    encoding = sys.getfilesystemencoding()
    args = [a.encode(encoding) for a in args]

    ghostscript.Ghostscript(*args)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.ps output.pdf")
        sys.exit(1)

    ps_file = sys.argv[1]
    pdf_file = sys.argv[2]

    try:
        ps_to_pdf(ps_file, pdf_file)
        print(f"Converted '{ps_file}' to '{pdf_file}'")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

