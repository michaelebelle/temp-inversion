import os
import xlsxwriter

def purge(lst):
    return [elem for elem in lst if elem != ""]

path = "/Users/michaelebelle/Documents/Inversion Folder/InversionProject"
workbook = xlsxwriter.Workbook('Inversion Data.xlsx')
worksheet = workbook.add_worksheet()

total_inversions = 0
for file in os.listdir("./"):
    if file.endswith(".txt") and file[:2] == "US":
        text = open(file, "r").read().split("\n")
        output = ""
        no_inversions = 0
        num_inversions = 0


        inversion_start = 0
        inversion_found = False
        date = 0
        last = 99999
        for line in text:
            line = purge(line.split(" "))
            if len(line) == 0:
                continue
            if "#" in line[0]:
                if line[1] + line[2] + line[3] == date:
                    inversion_start = 0
                else:
                    inversion_start = 0
                    if len(output) != 0 and not inversion_found:
                        output += "0\n"
                        no_inversions += 1
                        # print(file)


                    inversion_found = False
                    date = line[1] + line[2] + line[3]
                    output += line[2] + "/" + line[3] + "/" + line[1] + " "



                    # worksheet.write('B1', temp)
                    # worksheet.write('C1', last)

            elif not inversion_found:
                if "-9999" not in line[4] and "-9999" not in line[3] and "-8888" not in line[4] and "-8888" not in line[3]:
                    temp = 0
                    if "B" in line[4]:
                        temp = int(line[4][:line[4].find("B")])
                    elif "A" in line[4]:
                        temp = int(line[4][:line[4].find("A")])
                    if temp > last:
                        inversion_start += 1
                        if inversion_start > 3:
                            inversion_found = True
                            output += "1\n"
                            num_inversions += 1
                            total_inversions += 1
                            # print(file)
                    elif temp < last and inversion_start > 0:
                        inversion_start = 0
                    last = temp
        if not inversion_found:
            output += "0\n"


        # worksheet.write('A1', output)
        # worksheet.write('B1', temp)
        # worksheet.write('C1', last)


        # print("Hey")
        # print(output)

        # print(output)
        # print(" ", file)
        # print("Number of no inversion days:\t", no_inversions)
        # print("Number of inversion days:\t\t", num_inversions)
        # print("Number of days:\t\t\t\t\t", len(output.split('\n')) - 1)
        # print("\n")

workbook.close()