import time
import datetime
import winsound

def alarm():
    alarm_time = input('Enter the time of alarm to be set: HH:MM:SS M/D/YYYY')
    print('Alarm has been set for', alarm_time)
    alarm_form = datetime.datetime.strptime(alarm_time, '%H:%M:%S %m/%d/%Y')
    while True:
        now = datetime.datetime.now()
        if now >= alarm_form:
            print(f'Wake Up\nThe time is {now.strftime("%H:%M:%S %m/%d/%Y")}')
            winsound.PlaySound('wakeup.wav',
                               winsound.SND_FILENAME)
            # time.sleep(0)
            break
        else:
            print(f'The time is {now.strftime("%H:%M:%S %m/%d/%Y")}')
            time.sleep(1)


def main():
    alarm()

if __name__ == '__main__':
    main()