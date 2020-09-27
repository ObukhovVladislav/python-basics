# correct_result = '217.168.17.5'
correct_result1 = [
    '217.168.17.5',
    '- - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
]
result1 = row_record1.split(maxsplit=1)
print(result1)

row_record2 = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
correct_result2 = [
    '93.180.71.3',
    '- - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
]
result2 = row_record2.split(maxsplit=1)
print(result2)