
from test import check_ip
old_ip = "10.22.10.144"


if __name__ == "__main__":
    new_ip = check_ip()
    if old_ip != new_ip:
         print('ip_changed')
