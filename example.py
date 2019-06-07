from hostip import HostIP

hostip = HostIP()
ip = hostip.get_ip_info('8.8.8.8')

print("Showing details for google DNS\'s IP (8.8.8.8):")
print("Country: " + ip.country_name)
print("City and state: " + ip.city_and_state)
print("Coordinates: " + ip.coordinates)
