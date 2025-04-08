
def format_string():
    val = input("Enter your string: ")
    str_dict = val.split(".")
    print(str_dict)
    output_str = ""
    dict_upper_num = input("enter dict upper number")
    if dict_upper_num == "11":
        output_str += str_dict[0] + " "
        output_str += "- "
        for x in str_dict[4:6]:
            output_str += x + " "
        output_str += "- "
        for x in str_dict[6:len(str_dict)]:
            output_str += x + " "
        output_str.strip()
        print(output_str)
    elif dict_upper_num == "22":
        output_str += str_dict[0] + " "
        output_str += "- "
        for x in str_dict[4:9]:
            output_str += x + " "
        output_str += "- "
        for x in str_dict[9:len(str_dict)]:
            output_str += x + " "
        output_str.strip()
        print(output_str)
    else:
        dict_lower_num = input("enter dict lower number")
        author_upper_num = input("enter author upper number")
        author_lower_num = input("enter author lower number")
        name_upper_num = input("enter name upper number")
        name_lower_num = input("enter name lower number")
        
        if dict_upper_num != "n":
            for x in str_dict[int(dict_upper_num):int(dict_lower_num)+1]:
                output_str += x + " "
            output_str += "- "
        if author_upper_num != "n":
            for x in str_dict[int(author_upper_num):int(author_lower_num)+1]:
                output_str += x + " "
            output_str += "- "
        if name_upper_num != "n":
            for x in str_dict[int(name_upper_num):int(name_lower_num)+1]:
                output_str += x + " "
        output_str.strip()
        print(output_str)
    

def main():
    #iscontinue = True
    while True:
        format_string()
        #wantcontinue = input("Do you want to continue?")
        #iscontinue = bool(wantcontinue)

if __name__ == "__main__":
    main()