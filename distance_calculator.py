import googlemaps
from datetime import datetime
import time

# Google Maps API anahtarınızı buraya ekleyin
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Kullanıcıdan isim ve soyisim alın
name = input("Lütfen isminizi girin: ")
surname = input("Lütfen soyisminizi girin: ")

# Kullanıcıdan kalkış ve varış konumlarını alın
departure_location = input("Nereden gideceksiniz? (Örneğin: Mecidiyeköy, Istanbul) ")
arrival_location = input("Nereye gideceksiniz? (Örneğin: Kadıköy, Istanbul) ")

# Kullanıcıdan kalkış zamanını alın
departure_time_str = input("Ne zaman gideceksiniz? (HH:MM:SS formatında) ")

# Kullanıcıdan araç türünü alın
vehicle_type = input("Hangi araçla gideceksiniz? (driving, walking, bicycle, two-wheeler) ")

# Kalkış zamanını, 1970 yılı 1 Ocak'tan itibaren geçen saniye cinsinden hesaplayın
departure_time = datetime.strptime(departure_time_str, '%H:%M:%S')
departure_time_seconds = int(time.mktime(departure_time.timetuple()))

# Mesafeyi ve süreyi çekin
distance_result = gmaps.distance_matrix(departure_location, arrival_location, departure_time=departure_time_seconds, mode=vehicle_type)

# Mesafeyi ve süreyi yazdırın
print(f"Merhaba {name} {surname}, {departure_location} ile {arrival_location} arasındaki mesafe: {distance_result['rows'][0]['elements'][0]['distance']['text']}")
print(f"Yolculuk süresi: {distance_result['rows'][0]['elements'][0]['duration_in_traffic']['value']} saniye")