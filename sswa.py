version = 20240306.1

class parse:
    class rabbit1:
        def __init__(self, logfilename):
            self.log = []
            self.log.append([0, 'Opening supplied file'])
            try:
                logfile = open(logfilename)
                self.log.append([0, 'Opened ' + logfilename])
            except:
                self.log.append([2, 'Error opening ' + logfilename])
                return
            self.log.append([0, 'Initializing'])
            prevline = []
            self.stream = []
            self.frequency = []
            self.time = []
            self.location = []
            self.temperature = []
            self.humidity = []
            self.pressure = []
            linenum = 1
            self.log.append([0, 'Init done'])
            for liveline in logfile:
                if liveline[0] == "#":
                    self.log.append([0, 'Encountered comment on line ' + str(linenum)])
                    linenum += 1
                    continue
                liveline = liveline.replace('[', '').replace(']', '').replace(',\n', '').split(',')
                if prevline == []:
                    prevline = liveline
                    self.log.append([0, 'Building previous line buffer'])
                    linenum += 1
                    continue
                if liveline == ['f', 'da', 'db', 'dc', 'ga', 'go', 't', 'h', 'p']:
                    self.log.append([1, 'No data on line ' + str(linenum)])
                    linenum += 1
                    continue
                for i in range(9):
                    try:
                        liveline[i] = float(liveline[i])
                    except:
                        self.log.append([1, 'Line ' + str(linenum) + ' got "' + str(liveline[i]) + '". Using "' + str(prevline[i]) + '" from the last line.'])
                        liveline[i] = prevline[i]
                if liveline[4] == 0.0:
                    self.log.append([1, 'No GPS lock on line ' + str(linenum)])
                    linenum += 1
                    continue
                liveline[0] = liveline[0]
                liveline[1] = round(liveline[1])
                liveline[2] = round(liveline[2])
                liveline[3] = round(liveline[3])
                liveline[4] = round(int(str(liveline[4])[:2]) + float(str(liveline[4])[2:])/60, 6)
                liveline[5] = -round(int(str(liveline[5])[:2]) + float(str(liveline[5])[2:])/60, 6)
                liveline[6] = liveline[6]
                liveline[7] = liveline[7]
                liveline[8] = round(liveline[8])
                self.stream.append(liveline)
                self.time.append([liveline[1], liveline[2], liveline[3]])
                self.location.append([liveline[4], liveline[5]])
                self.temperature.append(liveline[6])
                self.humidity.append(liveline[7])
                self.pressure.append(liveline[8])
                prevline = liveline
                linenum += 1
            self.log.append([0, 'Cleaning up'])
            logfile.close()
            self.frequency = liveline[0]
            self.units = {'stream':['MHz','Time H','Time M','Time S','Degrees Latitude','Degrees Longitude','Degrees C','Percent','Pascals']}
            self.log.append([0, 'Program complete.'])
