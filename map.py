import sys
import struct
import binascii


################################# BALISE #################################



f2 = open("out.txt", "w")
shift = bytearray()
final_shift = 0


balise = {}
no = bytearray()
nom = bytearray()
freq = bytearray()
tp = bytearray()
lati = bytearray()
longi = bytearray()
decmag = bytearray()
alt = bytearray()
z = 1
i = 1 #byte counter
j = 1 #object counter
with open("DataBase/balise.si2", "rb") as f:

    while(byte := f.read(1)):
        z += 1

        if( i<= 4):             # Number of objects 4 bytes
            no += byte  
            i+=1             
        elif(i <= 12):             # NAME 8 bytes
            nom += byte
            i+=1
        elif(i <= 16):             # Frequency
            freq += byte
            i+=1
        elif(i <= 20):             # Type
            tp += byte      
            i+=1
        elif(i <= 28):             # Lat
            lati += byte
            i+=1
        elif(i <= 36):             # Long
            longi += byte
            i+=1
        elif(i <= 44):             # Dec Mag
            decmag += byte
            i+=1
        elif(i <= 52):             # Altitude
            alt += byte
            i+=1
        elif(i == 53):           # End of Object
            balise[j] = {}

            #Name
            name = ''
            for x in nom:
                if(x!= 0):
                    name += chr(x)
            nom = name.strip()

            #Frequency
            freq = str(struct.unpack('l', bytes.fromhex(str(freq.hex())))[0])
            freq = freq[:3] + "." + freq[3:]

            #Type
            tp = struct.unpack('l', bytes.fromhex(str(tp.hex())))[0]
            
            #Lat
            lati = str(struct.unpack('Q', bytes.fromhex(str(lati.hex())))[0])
            lati  = lati[:2] + "." + lati[2:]

            #Long
            longi = str(struct.unpack('Q', bytes.fromhex(str(longi.hex())))[0])    
            longi = longi[:1] + "." + longi[1:]

            #DecMag
            decmag = struct.unpack('d', bytes.fromhex(str(decmag.hex())))[0]

            #Altitude
            alt = str(struct.unpack('d', bytes.fromhex(str(alt.hex())))[0])

            #UPDATE DATABASE WITH THE NEW OBJECT
            balise[j]['name'] = nom
            balise[j]['freq'] = freq
            balise[j]['type'] = tp
            balise[j]['lati'] = lati
            balise[j]['longi'] = longi
            balise[j]['decmag'] = decmag
            balise[j]['alt'] = alt

            #PREPARE NEXT OBJECT
            name = ''
            nom = bytearray()
            freq = bytearray()
            tp = bytearray()
            lati = bytearray()
            longi = bytearray()
            decmag = bytearray()
            alt = bytearray()

            j += 1
            i = 6
            nom += byte
    
    f2.write(str(balise))

print("BALISE: ")
print(" - Helify: " + str(binascii.hexlify(no)))
print(" - Hex: " + str(no.hex()))
print(" - Struct: " + str(struct.unpack('l', bytes.fromhex(str(no.hex())))[0]))

f.close()
f2.close()



################################# WAYPOINT #################################

f_waypoint2 = open("waypoint.txt", "w")
waypoint = {}
no = bytearray()
nom = bytearray()
lati = bytearray()
longi = bytearray()

z = 1
i = 1 #byte counter
j = 1 #object counter

with open("DataBase/waypoint.si2", "rb") as f_waypoint:

    while(byte := f_waypoint.read(1)):
            
        if( i <= 4):             # Number of objects 4 bytes
            no += byte  
            i+=1             
        elif(i <= 12):             
            lati += byte
            i+=1
        elif(i <= 20):             
            longi += byte
            i+=1
        elif(i <= 28):         
            nom += byte
            i+=1
        elif(i == 29):      
            waypoint[j] = {}

            #Name
            name = ''
            for x in nom:
                if(x != 0):
                    name += chr(x)
            nom = name.strip()

            # Lat
            lati = str(struct.unpack('Q', bytes.fromhex(str(lati.hex())))[0])
            lati  = lati[:2] + "." + lati[2:]

            # Long
            longi = str(struct.unpack('Q', bytes.fromhex(str(longi.hex())))[0])    
            longi = longi[:1] + "." + longi[1:]   

            waypoint[j]['name'] = nom
            waypoint[j]['lati'] = lati
            waypoint[j]['longi'] = longi
            name = ''
            nom = bytearray()
            lati = bytearray()
            longi = bytearray()

            i = 6
            lati += byte
            z += 1
            j += 1

    f_waypoint2.write(str(waypoint))

print("WAYPOINTS: ")
print(" - Objects: " + str(z))
print(" - Hex: " + str(no.hex()))
print(" - Struct: " + str(struct.unpack('l', bytes.fromhex(str(no.hex())))[0]))

f_waypoint2.close()
f_waypoint.close()




################################# ILS #################################



f_ils2 = open("ils.txt", "w")

ils = {}
no = bytearray()
nom = bytearray()
freq = bytearray()
tp = bytearray()
lat_loc = bytearray()
long_loc = bytearray()
lat_gl = bytearray()
long_gl = bytearray()
lat_p1 = bytearray()
long_p1 = bytearray()
lat_p2 = bytearray()
long_p2 = bytearray()
axe = bytearray()
pente = bytearray()
decmag = bytearray()
alt = bytearray()
dist_dme = bytearray()
lat_in = bytearray()
long_in = bytearray()
lat_mid = bytearray()
long_mid = bytearray()
lat_out = bytearray()
long_out = bytearray()

z = 1
i = 1 #byte counter
j = 1 #object counter
with open("DataBase/ils.si2", "rb") as f_ils:

    while(byte := f_ils.read(1)):
        z += 1

        if( i <= 4):          # Number of objects 4 bytes
            no += byte  
            i+=1             
        elif(i <= 12):             # NAME 8 bytes
            nom += byte
            i+=1
        elif(i <= 16):             # Frequency
            freq += byte
            i+=1
        elif(i <= 20):             # Type
            tp += byte      
            i+=1
        elif(i <= 28):             # Lat
            lat_loc += byte
            i+=1
        elif(i <= 36):             # Long
            long_loc += byte
            i+=1
        elif(i <= 44):             # Dec Mag
            lat_gl += byte
            i+=1
        elif(i <= 52):             # Altitude
            long_gl += byte
            i+=1
        elif( i<= 60):             # Number of objects 4 bytes
            lat_p1 += byte  
            i+=1             
        elif(i <= 68):             # NAME 8 bytes
            long_p1 += byte
            i+=1
        elif(i <= 76):             # Frequency
            lat_p2 += byte
            i+=1
        elif(i <= 84):             # Type
            long_p2 += byte      
            i+=1
        elif(i <= 92):             # Lat
            axe += byte
            i+=1
        elif(i <= 100):             # Long
            pente += byte
            i+=1
        elif(i <= 108):             # Dec Mag
            decmag += byte
            i+=1
        elif(i <= 116):             # Altitude
            alt += byte
            i+=1
        elif( i<= 124):             # Number of objects 4 bytes
            dist_dme += byte  
            i+=1             
        elif(i <= 132):             # NAME 8 bytes
            lat_in += byte
            i+=1
        elif(i <= 140):             # Frequency
            long_in += byte
            i+=1
        elif(i <= 148):             # Type
            lat_mid += byte      
            i+=1
        elif(i <= 156):             # Lat
            long_mid += byte
            i+=1
        elif(i <= 164):             # Long
            lat_out += byte
            i+=1
        elif(i <= 172):             # Dec Mag
            long_out += byte
            i+=1
        elif(i == 173):           # End of Object
            ils[j] = {}

            #Name
            name = ''
            for x in nom:
                if(x!= 0):
                    name += chr(x)
            nom = name.strip()

            #Frequency
            freq = str(struct.unpack('l', bytes.fromhex(str(freq.hex())))[0])
            freq = freq[:3] + "." + freq[3:]

            #Type
            tp = struct.unpack('l', bytes.fromhex(str(tp.hex())))[0]
            
            #Lat Localizer
            lat_loc = str(struct.unpack('Q', bytes.fromhex(str(lat_loc.hex())))[0])
            lat_loc  = lat_loc[:2] + "." + lat_loc[2:]

            #Long Localizer
            long_loc = str(struct.unpack('Q', bytes.fromhex(str(long_loc.hex())))[0])    
            long_loc = long_loc[:1] + "." + long_loc[1:]

            #Lat Glide
            lat_gl = str(struct.unpack('Q', bytes.fromhex(str(lat_gl.hex())))[0])
            lat_gl  = lat_gl[:2] + "." + lat_gl[2:]

            #Long Glide
            long_gl = str(struct.unpack('Q', bytes.fromhex(str(long_gl.hex())))[0])    
            long_gl = long_gl[:1] + "." + long_gl[1:]

            #Lat P1
            lat_p1 = str(struct.unpack('Q', bytes.fromhex(str(lat_p1.hex())))[0])
            lat_p1  = lat_p1[:2] + "." + lat_p1[2:]

            #Long P1
            long_p1 = str(struct.unpack('Q', bytes.fromhex(str(long_p1.hex())))[0])    
            long_p1 = long_p1[:1] + "." + long_p1[1:]

            #Lat P2
            lat_p2 = str(struct.unpack('Q', bytes.fromhex(str(lat_p2.hex())))[0])
            lat_p2  = lat_p2[:2] + "." + lat_p2[2:]

            #Long P2
            long_p2 = str(struct.unpack('Q', bytes.fromhex(str(long_p2.hex())))[0])    
            long_p2 = long_p2[:1] + "." + long_p2[1:]

            #Axe
            axe = struct.unpack('d', bytes.fromhex(str(axe.hex())))[0]

            #Alfa
            pente = str(struct.unpack('d', bytes.fromhex(str(pente.hex())))[0])

            #Magnetic Declination
            decmag = struct.unpack('d', bytes.fromhex(str(decmag.hex())))[0]

            #Altitude
            alt = str(struct.unpack('d', bytes.fromhex(str(alt.hex())))[0])

            #DME Distance
            dist_dme = struct.unpack('d', bytes.fromhex(str(dist_dme.hex())))[0]

            #Lat Inner
            lat_in = str(struct.unpack('Q', bytes.fromhex(str(lat_in.hex())))[0])
            lat_in  = lat_in[:2] + "." + lat_in[2:]

            #Long Inner
            long_in = str(struct.unpack('Q', bytes.fromhex(str(long_in.hex())))[0])    
            long_in = long_in[:1] + "." + long_in[1:]

            #Lat Mid
            lat_mid = str(struct.unpack('Q', bytes.fromhex(str(lat_mid.hex())))[0])
            lat_mid  = lat_mid[:2] + "." + lat_mid[2:]

            #Long Mid
            long_mid = str(struct.unpack('Q', bytes.fromhex(str(long_mid.hex())))[0])    
            long_mid = long_mid[:1] + "." + long_mid[1:]

            #Lat Out
            lat_out = str(struct.unpack('Q', bytes.fromhex(str(lat_out.hex())))[0])
            lat_out  = lat_out[:2] + "." + lat_out[2:]

            #Long Out
            long_out = str(struct.unpack('Q', bytes.fromhex(str(long_out.hex())))[0])    
            long_out = long_out[:1] + "." + long_out[1:]

            #UPDATE DATABASE WITH THE NEW OBJECT
            ils[j]['name'] = nom
            ils[j]['freq'] = freq
            ils[j]['type'] = tp
            ils[j]['lat_loc'] = lat_loc
            ils[j]['long_loc'] = long_loc
            ils[j]['lat_gl'] = lat_gl
            ils[j]['long_gl'] = long_gl
            ils[j]['lat_p1'] = lat_p1
            ils[j]['long_p1'] = long_p1
            ils[j]['lat_p2'] = lat_p2
            ils[j]['long_p2'] = long_p2
            ils[j]['axe'] = axe
            ils[j]['pente'] = pente
            ils[j]['decmag'] = decmag
            ils[j]['alt'] = alt
            ils[j]['dist_dme'] = dist_dme
            ils[j]['lat_in'] = lat_in
            ils[j]['long_in'] = long_in
            ils[j]['lat_mid'] = lat_mid
            ils[j]['long_mid'] = long_mid
            ils[j]['lat_out'] = lat_out
            ils[j]['long_out'] = long_out  

            #PREPARE NEXT OBJECT
            name = ''
            nom = bytearray()
            freq = bytearray()
            tp = bytearray()
            lat_loc = bytearray()
            long_loc = bytearray()
            lat_gl = bytearray()
            long_gl = bytearray()
            lat_p1 = bytearray()
            long_p1 = bytearray()
            lat_p2 = bytearray()
            long_p2 = bytearray()
            axe = bytearray()
            pente = bytearray()
            decmag = bytearray()
            alt = bytearray()
            dist_dme = bytearray()
            lat_in = bytearray()
            long_in = bytearray()
            lat_mid = bytearray()
            long_mid = bytearray()
            lat_out = bytearray()
            long_out = bytearray()

            j += 1
            i = 6
            nom += byte
    
    f_ils2.write(str(ils))

print("ILS: ")
print(" - Helify: " + str(binascii.hexlify(no)))
print(" - Hex: " + str(no.hex()))
print(" - Struct: " + str(struct.unpack('l', bytes.fromhex(str(no.hex())))[0]))

f_ils.close()
f_ils2.close()