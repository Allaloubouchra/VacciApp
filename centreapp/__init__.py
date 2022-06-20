class DayOfWeek:
    SATURDAY = 5
    SUNDAY = 6
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    WEEKDAYS = (
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Thursday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
    )


class Temperature:
    FEBRILE = "F"
    APYRETIQUE = "A"
    CHOICES = (
        (FEBRILE, "Fébrile"),
        (APYRETIQUE, "Apyrétique"),
    )


class FreqCardiaque:
    TACHYCARDIE = "T"
    NORMAL = "N"
    BRADYCARDIE = "B"

    CHOICES = (
        (TACHYCARDIE, "Tachycardie"),
        (NORMAL, "Normal"),
        (BRADYCARDIE, "Bradycardie"),
    )


class FreqRespi:
    EUPNEIQUE = "E"
    DYSPNEE = "D"
    BRADYPNEE = "B"

    CHOICES = (
        (EUPNEIQUE, "Eupneique"),
        (DYSPNEE, "Dyspnée"),
        (BRADYPNEE, "Bradypnée"),
    )


class Tension:
    HYPERTENSION = "H"
    NORMAL = "N"
    HYPOTENSION = "O"

    CHOICES = (
        (HYPERTENSION, "Hypertension"),
        (NORMAL, "Normal"),
        (HYPOTENSION, "Hypotension"),
    )


class Saturation:
    GOOD = "G"
    BAD = "B"

    CHOICES = (
        (GOOD, "Bonne saturation"),
        (BAD, "Désaturation"),
    )
