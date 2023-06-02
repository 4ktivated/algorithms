def valid_ip(ip):
    ip_int = [int(i) for i in ip.split('.') if i.isdigit()]
    if len(ip.split('.')) > len(ip_int):
        return False
    else: 
        return (all(map(lambda x: 0 <= int(x) <= 255, ip_int))) 


ip = '10.1.1.a'
print(valid_ip(ip))