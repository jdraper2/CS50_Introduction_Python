def main():
    while True:
        try:
            fraction = input("Fraction: ")
            reading_values = convert(fraction)
            if reading_values != False:
                break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(reading_values))


def convert(fraction):

    try:
        reading = fraction.split("/")
        if int(reading[0]) > int(reading[1]):
            raise ValueError("ValueError")
        reading = int(reading[0]) / int(reading[1])
        return round(reading * 100)
    except ValueError:
        raise ValueError("ValueError")
    except ZeroDivisionError:
        raise ZeroDivisionError("ZeroDivisionError")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
