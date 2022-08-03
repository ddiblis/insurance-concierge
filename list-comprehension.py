import re
import json

try:
    insurance_company_list = open("list.txt", 'r')
    company_list = insurance_company_list.read()
    reg = re.findall(
        "(?P<ranking>[\d]+)	(?P<name>[\w \.\(\)-]+)	(?P<website>(www\.)?[\w-]+\.[\w]+)", company_list)
    dic = {}
    for r in reg:
        dic[r[1]] =  {
                "ranking": r[0],
                "website": r[2],
            }
    with open('companies.json', 'a') as outfile:
        outfile.write(json.dumps(dic, indent=4))
finally:
    insurance_company_list.close()
