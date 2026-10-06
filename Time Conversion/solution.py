from datetime import datetime


def timeConversion(time_string):
    """Convert a 12-hour time string to 24-hour format."""
    return datetime.strptime(time_string, "%I:%M:%S%p").strftime("%H:%M:%S")


if __name__ == "__main__":
    print(timeConversion("07:05:45PM"))
