import operator

def extract_ip_count_freq(filename): 
    file = open(filename, 'r')              #opening the file for reading
    ip_dict = dict()                        #storing the count of each ip address
    for line in file.readlines():           #reading the file's contents
        ip = line.split('- -')[0].strip()   #getting the first element of the array
        try: 
            tmp = ip_dict[ip]               #obtaining previous count if present
            tmp +=1                         #incrementing it
            ip_dict[ip] = tmp               #reassigning the ip to the corresponding ip key
        except:
            ip_dict[ip] = 1                 #storing the ip and giving it a count of 1
    return ip_dict 

def max_count_ip(ips): 
    sorted_ips = dict(sorted(ips.items(), key=operator.itemgetter(1), reverse = True)) 
    max_ip = list(sorted_ips.keys())[0]     #obtaining the most frequent ip address
    return max_ip, sorted_ips[max_ip]       #returning the ip and its count

def main():
    filename = 'full_log.txt'               
    ips = extract_ip_count_freq(filename)   #getting the ips and counts
    max_freq_ip, frq = max_count_ip(ips)    #getting the ip with the highest count
    print ('IP: {} comes {} in the file'.format(max_freq_ip, frq))

if __name__ == "__main__":
    main()
   
