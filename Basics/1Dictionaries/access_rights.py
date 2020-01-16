dict_files = dict()
number_files = int(input())

for i in range(number_files):
    file_names_and_allowed_operations = list(input().split())
    dict_files[file_names_and_allowed_operations[0]] = set(file_names_and_allowed_operations[1:])

number_operations_to_the_files = int(input())

actions_to_rights = {
'read': 'R',
'write': 'W',
'execute': 'X'
}


for k in range(number_operations_to_the_files):
    operation, filename = input().split()
    if actions_to_rights[operation] in dict_files[filename]:
        print("OK")
    else:
        print("Access denied")
    #for key_files, possible_operations in dict_files.items():
#
 #       if key_files == list_operations_with_file[1] and str(list_operations_with_file[0])[0].upper() in \
  #              possible_operations and len(str(list_operations_with_file[0])) <= 5:
   #         print("OK")
#
 #       if key_files == list_operations_with_file[1] and str(list_operations_with_file[0])[1].upper() in \
  #              possible_operations and len(str(list_operations_with_file[0])) > 5:
   #         print("OK")

    #    elif key_files == list_operations_with_file[1] and str(list_operations_with_file[0])[0].upper() not in possible_operations:
     #       print("Access denied")
#
 #       else:
  #          continue

#print(dict_files)
