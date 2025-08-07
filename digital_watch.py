import datetime
import time
import winsound

def menu():
    print('='*10,'Digital Watch','='*10)
    print('1.Show Time')
    print('2.Stopwatch')
    print('3.Alarm')
    print('4.Exit')
    choice = int(input('Enter your choice: '))
    return choice

def show_time():
    while True:
        actual_time = datetime.datetime.now()
        show_form_time = actual_time.strftime('%H:%M:%S')
        print(f'Current time is {show_form_time}')
        time.sleep(1)

        show_time_input = input('Press e to stop showing time or enter to show time again:')
        if show_time_input == 'e':
            print('Time stopped')
            break


def stopwatch():
    while True:
        start_input = input('Press s to start stopwatch')
        if start_input == 's':
            start_time = time.time()
            while True:
                end_input = input('Press e to end stopwatch')
                if end_input == 'e':
                    end_time = time.time()
                    total_time = end_time - start_time
                    print(f'Elapsed time: {total_time:.2f} seconds')
                    break
            break
        break
def alarm():
    while True:
        alarm_input = input('Press y/n to set alarm')
        if alarm_input == 'y':
            alarm_time = input('Enter the time of alarm in 24 hour format:(HH:MM): ')
            try:
                alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M').time()
                print(f'Alarm set for {alarm_time.strftime("%H:%M")}')
                while True:
                    current_time = datetime.datetime.now().time()
                    if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                        print('Wake up!')
                        alarm_sound = 'alarm.wav'
                        winsound.PlaySound(alarm_sound, winsound.SND_ASYNC)
                        alarm()
            except ValueError:
                print('Invalid time format, please try again')
        else:
            break
        break
def main():
    while True:
        choice = menu()
        if choice == 1:
            show_time()
        elif choice == 2:
            stopwatch()
        elif choice == 3:
            alarm()
        elif choice == 4:
            print('Thank you for using the clock App')
            break


if __name__ == '__main__':
    main()