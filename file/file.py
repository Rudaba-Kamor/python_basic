Name=input("What is your name?: ")
Address=input("Give your address: ")


#Query_file=open("C:\java_mylibrary\ file2.txt", "a")

Query_file=open("https://drive.google.com/drive/folders/1zO9CdAIMjjbg67hKe4cjDgqVBUiLGRCP/file2.pdf", "a")

Query_file.write("The name: "+ Name + " and the address: "  + Address)
Query_file.close()

Query_file=open("https://drive.google.com/drive/folders/1zO9CdAIMjjbg67hKe4cjDgqVBUiLGRCP/file2.pdf","r")
print(Query_file.read())
