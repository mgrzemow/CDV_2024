# SQL injection:
country = "Poland'); DROP TABLE osoby;--"

sql = f"""
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', '{country}');
"""

print(sql)