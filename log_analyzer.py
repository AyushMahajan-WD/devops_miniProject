
#Return the occurance of keyword
def occurance():
    path = input("Enter file path: ")
    keyword = input("Enter the occurance you want to check: ")
    count=0
    with open(f"{path}","r") as log_file:
        for item in log_file:
            count+= item.split().count(keyword)
    return count



#Print the last 10 lines of log
def return_ten_lines():
    path = input("Enter file path: ")
    with open(f"{path}","r") as log_file:
        log_var = log_file.read()
    count=0
    for i in log_var:
        if(i == "\n"):
            count+=1
    print(count)
    line_count = count

    with open(f"{path}","r") as log:
        for i in range(count+1):
            if(line_count<=10):
                line_data = log.readline()
                print(line_data,end = "")
                line_count-=1
            else:
                line_data = log.readline()
                line_count-=1
                
            

select = input('''Select below option:
1. Occurance of keyword
2. Print last 10 lines 
''')
if(select == "1"):
    print(occurance())
elif(select == "2"):
    return_ten_lines
else:
    print("Select valid option")
