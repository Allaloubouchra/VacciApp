from django.utils.translation import gettext_lazy as _


class UserType:
    PATIENT = "P"
    DOCTOR = "D"
    RECEPTIONIST = "R"

    USER_TYPE_CHOICES = (
        (PATIENT, _("Patient")),
        (DOCTOR, _("Doctor")),
        (RECEPTIONIST, _("Receptionist")),
    )


class GenderType:
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )


class AppointmentStatus:
    PENDING = 'PE'
    CONFIRMED = 'CO'
    CANCELED = 'CA'
    DONE = 'DO'

    STATUS_CHOICES = (
        (PENDING, _('Pending')),
        (CONFIRMED, _('Confirmed')),
        (CANCELED, _('Canceled')),
        (DONE, _('Done')),
    )


class Arms:
    RIGHT = 'R'
    LEFT = 'L'

    ARMS_CHOICES = (
        (RIGHT, _('Right')),
        (LEFT, _('Left')),
    )
