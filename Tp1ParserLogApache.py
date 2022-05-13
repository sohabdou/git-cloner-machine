from pprint import pprint
import json
import re

ip_count = {}
with open("./access.log", "r") as file_pointer:
    lines = file_pointer.readlines()
    for l in lines:
        regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.+\] \".+\" (\d{3}) \d+ "
        ip, status = re.findall(regex, l)[0]

        if ip not in ip_count:
            ip_count[ip] = {}

        if status in ip_count[ip]:
            ip_count[ip][status] += 1
        else:
            ip_count[ip][status] = 1

with open("ip_status.json", "w") as file:
    json.dump(ip_count, file, indent=2)




# # lecture du fichier
# from pprint import pprint                                        # formater le print avec des sauts à la ligne
# import re                                                        # regex
# import json
#
# ip_count = {}                                                    # definition de dictionnaire vide
# with open("./access.log", "r") as file_pointer:                  #ouvrir le fichier temporairement
#     lines = file_pointer.readlines()                             #
#     for l in lines:
#         regexp =r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.+\] \".+\" (\d{3}) \d+ "
#     # codehttp = r"\[.+\] \".+\" (\d{3}) \d+ "
#     # for l in lines:
#     #     ips_list = re.findall(regexp, l), re.findall(codehttp,l)
#     #     pprint(ips_list)
#     #     status = re.findall(regexp, l)[0]
#         ips_list = re.findall(regexp, l)[0]
#         if ips_list in ip_count:                                  # compter(verification) le nombre adresse ip
#             ip_count[ips_list] += 1                               # incrémenter de 1
#         else:
#              ip_count[ips_list] = 1                                # rajouter l'ip ssi n'existe pas
#
# # pprint(ip_count)
#
# with open("access.json", "w") as json_file_pointer:             # Lecture mode json
#     sorted_string = json.dumps(str(ip_count), indent=4, sort_keys=True)
#     json.dump(sorted_string, json_file_pointer)                      #  indent=4, sort_keys=True
#
# # print("Started writing JSON data into a file")
# # with open("access.json", "w") as write_file:
# #     json.dump(acce, write_file) # encode dict into JSON
# # print("Done writing JSON data into .json file")
# pprint(ip_count)

