device_status = "active"
temperature = 41

if device_status == "active":
    if temperature > 35:
        print("High temperature Alert!")
    else:
        print("Temperature is Normal")
else:
    print("Device is Offline")