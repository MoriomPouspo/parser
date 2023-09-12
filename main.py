import csv
import pymongo

attributes = [
    {'name': 'Gender', 'type': 'string', 'domain': '{"M","F"}'},
    {'name': 'AgeBaseline', 'type': 'int', 'domain': '[0, 100]'},
    {'name': 'HTNmeds', 'type': 'int', 'domain': '{0,1}'},
    {'name': 'ACEIARB', 'type': 'int', 'domain': '{0,1}'},
    {'name': 'CholesterolBaseline', 'type': 'float', 'domain': '{2.23, ...,9.3}'},
    {'name': 'HistoryDiabetes', 'type': 'bool'},
    {'name': 'HistoryCHD', 'type': 'bool'},
    {'name': 'HistoryVascular', 'type': 'bool'},
    {'name': 'HistorySmoking', 'type': 'bool'},
    {'name': 'HistoryHTN', 'type': 'bool'},
    {'name': 'HistoryDLD', 'type': 'bool'},
]

print("Attributes")
for attr in attributes:
    print("|", attr)

data_list = []
with open('dummy_data.csv', 'r') as csv_file:
    # Create a CSV DictReader object
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        data = {'id': row['id'], 'date': row['date'], 'patientname': row['patientname'], 'drname': row['drname']}

        for attr in attributes:
            value = ''
            if attr['name'] in row:
                value = row[attr['name']]

            data[attr['name']] = value

        data_list.append(data)


# Establish a connection to your MongoDB server
client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/?authMechanism=DEFAULT")

# Select a database and collection
db = client["medchain"]
collection = db["diagnostics"]

# Insert the list of dictionaries into the collection
result = collection.insert_many(data_list)

# Print the inserted document IDs
print("Inserted document IDs:", result.inserted_ids)
