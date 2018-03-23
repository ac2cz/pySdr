from scipy.io import wavfile

def get_double_from_int(value):
    if (value > (2^15-1)):
        value = (-1*2^16) + value
    value = value /32768.0;
    return value

def main():
    [fs, x] = wavfile.read("test_sound.wav")
    print ('Wavefile: Sample Rate: ', fs)

    for i in x:
        print(get_double_from_int(i[0]))
        
main()
