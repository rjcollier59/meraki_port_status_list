import csv
import functions 

switches = []
ports = []
orgs = functions.get_orgs()

inventory = functions.get_inventory(orgs[0]["id"])
networks = functions.get_networks(orgs[0]["id"])

for device in inventory:
    if device["model"].startswith("MS"):
        temp = {}
        temp["serial"] = device["serial"]

        for network in networks:
            if device["networkId"] == network["id"]:
                temp["network"] = network["name"]



        for x in range(1,55):
            temp[x] = " "

        list_ports = functions.get_switch_ports(device["serial"])
        print(list_ports)

        for index,port in enumerate(list_ports,start=1):
            try:
                temp[index] = port["status"]
                ports.append(temp)
            except:
                temp[index] = " "
                continue

keys = ports[0].keys()
with open('ports.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(ports)
