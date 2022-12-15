# Script to ask the user to input IPv4 address and covert it to a binary notation

ipv4Dec = input("Please enter IPv4 Address: ")
print(ipv4Dec)
# Testing type of ipv4Dec variable
# print(type(ipv4Dec))

# Split entered IPv4 address into four octets
firstOctet = int(ipv4Dec.split('.')[0])
secondOctet = int(ipv4Dec.split('.')[1])
thirdOctet = int(ipv4Dec.split('.')[2])
fourthOctet = int(ipv4Dec.split('.')[3])

# Print the binary notation of entered IPv4 address
print('The IPv4 address {0} in dotted binary notation is: {1:08b}.{2:08b}.{3:08b}.{4:08b}'.format(ipv4Dec, firstOctet, secondOctet, thirdOctet, fourthOctet))