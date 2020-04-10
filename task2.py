seconds = int(input("Введите время в секундах.\n"))

seconds: int = seconds
minutes: int = seconds / 3600
hours: int = (seconds / 3600) / 60

result = '{0}:{1}:{2}'.format(hours, minutes, seconds)

print(result)