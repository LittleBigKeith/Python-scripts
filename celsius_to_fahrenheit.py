celsius_min = 0
celsius_max = 100
step = 10
print('Celsius\tFahrenheit')
for celsius in range(celsius_min, celsius_max + step, step):
    farhenheit = celsius / 5 * 9 + 32
    print(f'{celsius:7}\t{farhenheit:10.0f}')