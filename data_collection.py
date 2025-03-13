import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_foreign_satellites_launched_by_India"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

tables = soup.find_all("table", {"class": "wikitable"})

satellites = []

#processing each table
for table in tables:
    rows = table.find_all("tr")[1:]  
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 6:  
            # extracting data from each column
            no = cols[0].text.strip()
            name = cols[1].text.strip()
            country = cols[2].text.strip()
            launch_date = cols[3].text.strip()
            launch_mass = cols[4].text.strip().replace("kg", "").strip()  
            launch_vehicle = cols[5].text.strip()
            remarks = cols[6].text.strip() if len(cols) > 6 else ""

            # extracting the year from the launch date
            year = pd.to_datetime(launch_date, errors='coerce').year if launch_date else None

            satellites.append({
                "no": no,
                "name": name,
                "country": country,
                "launch_date": launch_date,
                "launch_mass": launch_mass,
                "launch_vehicle": launch_vehicle,
                "remarks": remarks,
                "year": year
            })

# Convert to DataFrame
df = pd.DataFrame(satellites)

df["launch_date"] = pd.to_datetime(df["launch_date"], errors="coerce")

df["launch_mass"] = pd.to_numeric(df["launch_mass"], errors="coerce")

df.to_csv("foreign_satellites_by_india.csv", index=False) #saving to csv
print("Data successfully saved to CSV!")


    







