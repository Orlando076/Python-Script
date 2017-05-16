import csv
import datetime
import time
#----------------------------------------------------------------------
def csv_writer(data, path):
    """Write data to a CSV file path"""
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
#----------------------------------------------------------------------
if __name__ == "__main__":
    """datatest = "D218410,Gianni,de Waal,Aanwezig," """
    var timestamp = time.strftime('%H-%M-%S')
    data = ["Studentnummer,Voornaam,Achternaam,Presentie,Tijd".split(","),
            "D218410,Gianni,de Waal,Aanwezig,tijdstip".split(",")
           ]
    path = "Aanwezigheid "+time.strftime("%Y-%m-%d")+".csv"
    print("tijdstip "+time.strftime('%H:%M:%S'))
    csv_writer(data, path)