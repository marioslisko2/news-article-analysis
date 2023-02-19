import hashlib

output_file_path = "C:/Users/mario/OneDrive/Radna površina/Faks/UPZ/scrap/praviLinkovi.txt"
input_file_path = "C:/Users/mario/OneDrive/Radna površina/Faks/UPZ/scrap/linkovi.txt"

completed_lines=set()

output_file = open(output_file_path,"w")

for line in open(input_file_path,"r"):

    hashValue = hashlib.md5(line.rstrip().encode('utf8')).hexdigest()

    if hashValue not in completed_lines:
            output_file.write(line)
            completed_lines.add(hashValue)

output_file.close()