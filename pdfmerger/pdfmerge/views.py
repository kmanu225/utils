import os
from django.shortcuts import render
from django.http import FileResponse
from pypdf import PdfWriter
from django.core.files.storage import default_storage

def merge_pdfs(request):
    if request.method == "POST":
        files = request.FILES.getlist("pdfs")
        print("Uploaded files:", files)  # debug print

        if not files:
            return render(request, "merge.html", {"error": "No files uploaded."})

        merger = PdfWriter()
        file_paths = []

        # Save uploaded files temporarily
        for f in files:
            path = default_storage.save(f.name, f)
            file_paths.append(default_storage.path(path))

        # Merge PDFs
        for pdf in file_paths:
            merger.append(pdf)

        # Write merged PDF
        output_path = default_storage.path("merged.pdf")
        with open(output_path, "wb") as out:
            merger.write(out)
        merger.close()
        
        # Delete uploaded files
        for path in file_paths:
            if os.path.exists(path):
                os.remove(path)

        # Serve merged PDF for download
        return FileResponse(open(output_path, "rb"), as_attachment=True, filename="merged.pdf")

    return render(request, "merge.html")
