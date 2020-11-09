import threading
import socket


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        connection = s.connect((target, port))
        print('Port :', port, "is open.")
        connection.close()
    except:
        pass


ports = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,
         194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
         3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]

print('-' * 35)
target = input('Enter host:\n\n')
print('-' * 35)

for element in ports:
    t = threading.Thread(target=portscan, kwargs={'port': element})

    t.start()

input()
