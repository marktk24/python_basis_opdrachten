# import psutil
try:
    import psutil
except ImportError as e:
    print("psutil is not installed.")
    print("please install psutil.")
    exit()

adapters = psutil.net_if_addrs().items()

for adapter in adapters:
    print(adapter[0])

    for info in adapter[1]:
        if info[0] == 2:
            print(info[1])
    print("________________________")

