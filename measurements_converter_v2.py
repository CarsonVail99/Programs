class MeasurementsConverter:
    METRIC_CONVERSIONS = {
        'km':{'m':1000, 'cm':100000, 'mm':1000000},
        'm':{'km':0.001, 'cm':100, 'mm':1000},
        'cm':{'km':0.00001, 'm':0.01, 'mm':10},
        'mm':{'km':0.000001, 'm':0.001, 'cm':0.1}
    }

    IMPERIAL_CONVERSIONS = {
        'mile': {'yards': 1760, 'foot': 5280, 'inch': 63360},
        'yard': {'mile':0.000568182, 'foot': 3, 'inch': 36},
        'foot': {'mile':0.000189394, 'yard':0.33333333, 'inch': 12},
        'inch': {'mile':0.0000157828, 'yard':0.0277778, 'foot': 0.08333333}
    }

    UNITS = {
        '1': ('km', 'kilometer'),
        '2': ('m', 'meter'),
        '3': ('cm', 'centimeter'),
        '4': ('mm', 'millimeter'),
        '5': ('mile', 'miles'),
        '6': ('yard', 'yards'),
        '7': ('foot', 'feet'),
        '8': ('inch', 'inches')
    }
    @staticmethod
    def get_user_choice(prompt):
        while True:
            print('\n'.join([
                'What would you like to convert?',
                '1.Kilometers', '2.Meters',
                '3.Centimeters', '4.Millimeters',
                '5.Miles', '6.Yards',
                '7.Feet', '8.Inches'
            ]))
            choice = input(prompt).strip()
            if choice in MeasurementsConverter.UNITS:
                return choice
            print('please enter a number between 1 and 8')


    def get_value(self, unit_name):
        while True:
            try:
                value = float(input(f'Enter the value in {unit_name}: '))
                if value > 0:
                        return value
                print('Please enter a positive number')
            except ValueError:
                print(ValueError)
    def convert(self, value,from_unit, to_unit):
        if from_unit == to_unit:
            return value

        if from_unit in self.METRIC_CONVERSIONS and to_unit in self.METRIC_CONVERSIONS:
            return value * self.METRIC_CONVERSIONS[from_unit][to_unit]
        elif from_unit in self.IMPERIAL_CONVERSIONS and to_unit in self.IMPERIAL_CONVERSIONS:
            return value * self.IMPERIAL_CONVERSIONS[from_unit][to_unit]
        else:
            if from_unit in self.METRIC_CONVERSIONS:
                #convert to meters first
                meters = self.convert(value,from_unit, 'm')
                inches = meters * 39.3701
                return self.convert(inches, 'inch', to_unit)
            else:
                inches = self.convert(value,from_unit, 'inch')
                meters = inches / 39.3701
                return self.convert(meters, 'm', to_unit)

    def run(self):
        while True:
            try:
                from_choice = self.get_user_choice('From: ')
                from_unit, from_name = self.UNITS[from_choice]
                value =  self.get_value(from_name)

                to_choice = self.get_user_choice('To: ')
                to_unit, to_name = self.UNITS[to_choice]

                result = self.convert(value,from_unit, to_unit)
                print(f'\n{value} {from_name} = {result:4f} {to_name}')

                if input('Continue? (y/n) ').lower() != 'y':
                    break

            except ValueError:
                print(ValueError)

def main():
    converter = MeasurementsConverter()
    converter.run()

if __name__ == '__main__':
    main()