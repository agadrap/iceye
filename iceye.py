import binascii

def bytes_from_file(filename, chunksize=2068):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

if __name__ == '__main__':
    binary_data = []
    time = []
    lat = []
    long = []
    alt = []

# Managed to retrieve data as bytes, however I couldn't find correct encoding
# to see what exactly is written (I tried 'ascii', 'utf-8', 'itf-16' & 'latin-1')
# therefore I failed to split it and write it to an array based on csv structure
# so that I would be able to filter out the time, position etc.

    for b in bytes_from_file('telemetry.bin'):
        binary_data.append(b)

    print('Sample of binary_data: \n{}'.format(binary_data[:100]))
    print('Number of lines based on data chunk provided: \n{}'.format(len(binary_data)/2068))

# I have chosen the ephemeris file format - 'EphemerisLLATimePos':
# TimeInSeconds Lat Lon Alt
# but I could write only to .txt extension

    with open('stk.txt', 'w') as f:
        f.write('stk.v.5.0' + '\n')
        f.write('BEGIN Ephemeris' + '\n')
        f.write('NumberOfEphemerisPoints 3632' + '\n')
        f.write('ScenarioEpoch           1 Jan 2000 00:00:00.000000000' + '\n')
        f.write('InterpolationMethod     Lagrange' + '\n')
        f.write('InterpolationOrder      1' + '\n')
        f.write('DistanceUnit      Kilometers' + '\n')
        f.write('CentralBody             Earth' + '\n')
        f.write('CoordinateSystem        J2000' + '\n')
        f.write('EphemerisLLATimePos' + '\n')
        for index,value in enumerate(time):
            f.write('{} {} {} {}'.format(time[index], lat[index], lon[index], alt[index])+ '\n')
        f.write('END Ephemeris')

    with open('stk.txt','r') as f:
        for line in f:
            print(line)
