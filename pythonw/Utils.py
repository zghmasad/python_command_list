def prepend_to_file(file,str1):
    with open(file, 'r') as fin:
        #data = fin.read().splitlines(True)
        data=fin.readlines()
    with open(file, 'w') as fa:
        fa.write(str(str1)+'\n')
        fa.writelines(data[:-1])
        
# prepend_to_file('pythonw/test2.xml','ali sayfi5')
