bytes_value = int(input("Enter size in bytes: "))

kb = bytes_value / 1024
mb = kb / 1024
gb = mb / 1024

print("Size in KB:", kb)
print("Size in MB:", mb)
print("Size in GB:", gb)
