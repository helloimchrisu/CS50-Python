def main():
    fileName = input("File name: ")
    if fileName.endswith(".gif") == True:
        print("image/gif")
    elif fileName.endswith(".jpg") == True or fileName.endswith(".jpeg") == True:
        print("image/jpeg")
    elif fileName.endswith(".png") == True:
        print("image/png")
    elif fileName.endswith(".pdf") == True:
        print("application/pdf")
    elif fileName.endswith(".txt") == True:
        print("text/plain")
    elif fileName.endswith(".zip") == True:
        print("application/zip")
    else:
        print("application/octet-stream")
    
main()
