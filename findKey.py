nums = [71, 105, 207, 218, 498, 586, 638, 657, 671, 903, 910, 959, 1065, 1367, 1386, 1398, 1405, 1410, 1412, 1413, 1419, 1424, 1426, 1431, 1433, 1434, 1437, 1438, 1456, 1472, 1486, 1490, 1499, 1511, 1513, 1520, 1521, 1523, 1525, 1526, 1527, 1530, 1532, 1534, 1541, 1543, 1546, 1553, 1554, 1556, 1559, 1560, 1561, 1566, 1571, 1575, 1578, 1580, 1582, 1583, 1585, 1587, 1590, 1593, 1594, 1596, 1599, 1600, 1601, 1608, 1609, 1610, 1613, 1616, 1617, 1623, 1626, 1630, 1633, 1635, 1639, 1644, 1649, 1652, 1659, 1660, 1666, 1669, 1670, 1677, 1678, 1679, 1685, 1690, 1692, 1693, 1695, 1704, 1711, 1712, 1713, 1730, 1734, 1736, 1738, 1739, 1741, 1752, 1754, 1757, 1764, 1772, 1773, 1775, 1777, 1780, 1784, 1791, 1795, 1796, 1798, 1799, 1801, 1806, 1819, 1826, 1832, 1833, 1837, 1847, 1849, 1854, 1856, 1857, 1863, 1865, 1866, 1867, 1872, 1883, 1884, 1886, 1893, 1904, 1908, 1916, 1917, 1922, 1923, 1927, 1930, 1933, 1940, 1941, 1942, 1945, 1946, 1947, 1948, 1953, 1955, 1957, 1958, 1959, 1960, 1961, 1962, 1964, 1965, 1968, 1969, 1972, 1973, 1975, 1976, 1977, 1978, 1980, 1982, 1983, 1984, 1985, 1986, 1987, 1990, 1991, 1992, 1993, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2005, 2007, 2009, 2010]

found = False

for i in nums:
    for j in nums:
        if i + j == 2020:
            print("Found")
            print(i)
            print(j)
            x = i
            y = j
            found = True
            break
    if found:
        break
        


key = i*j
print(key)
