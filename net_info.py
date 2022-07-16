import psutil

def net_info():
    interfaces = psutil.net_if_addrs()
    for iface_name, iface_address in interfaces.items():
        for addr in iface_address:
            if str(addr.family) == 'AddressFamily.AF_INET':
                print(addr.family)
                print(f'Interface: {iface_name}\n')
                print(f'    IP Address: {addr.address}')
                print(f'    Netmask: {addr.netmask}')
                print(f'    Broadcast IP: {addr.broadcast}\n')
            elif str(addr.family) == 'AddressFamily.AF_INET6':
                print(addr.family)
                print(f'Interface: {iface_name}\n')
                print(f'    IP Address: {addr.address}')
                print(f'    Netmask: {addr.netmask}')
                print(f'    Broadcast IP: {addr.broadcast}\n' )
            elif str(addr.family) == 'AddressFamily.AF_LINK':
                print(addr.family)
                print(f'Interface: {iface_name}\n')
                print(f'    MAC Address: {addr.address}')
                print(f'    Netmask: {addr.netmask}')
                print(f'    Broadcast MAC: {addr.broadcast}\n' )

net_info()