import os


def rename_files():
    file_list = os.listdir(r"C:\Users\minch")
    # list directory
    saved_path = os.getcwd()
    # current working directory
    print("Current folder : " + saved_path)
    os.chdir(r"C:\Users\minch")
    for file_name in file_list:
        print("Original name : " + file_name)
        print("Modified name : " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)


rename_files()
