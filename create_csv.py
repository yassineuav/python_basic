import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 33.34])
#     writer.writerow([1002, 2, 23.23])
#     writer.writerow([1003, 1, 13.12])
#     writer.writerow([1004, 3, 33.12])
#     writer.writerow([1005, 1, 32.22])

with open("data.csv") as file:
    reader = csv.reader(file)
    #print(list(reader))
    
    for row in reader:
        print(row)
