def split_return(line):
    print(line)
    line = line.split("=")
    line = line[1]
    return line

def read():
    file_lines = open("config.txt","r").readlines()
    
    mon_mode = split_return(file_lines[0])
    def_iface = split_return(file_lines[3])

    config = {"mon": mon_mode, "iface": def_iface}
    return config
