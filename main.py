from pypdf import PdfWriter
try:
    merger = PdfWriter()
    pdfs=[]
    n = int(input("Enter the no of pdf you want to merge:"))
    for i in range(n):
        name=input(f"Enter the name of pdf {i+1}:")
        pdfs.append(name)
    for pdf in pdfs:
        merger.append(pdf)

    merger.write("all_merged.pdf")
    print("pdfs merged and saved as 'all_merged.pdf'")
except Exception as e :
    print(e)
