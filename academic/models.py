from django.db import models

# Create your models here.

from django.contrib.auth.models import User


SUBJECT_CHOICES = (
    ('Eco', 'Economics'),
    ('Art', 'Art'),
    ('Eng', 'English'),
    ('Mat', 'Maths'),
    ('Bio', 'Biology'),
    ('Phy', 'Physics'),
    ('Che', 'Chemistry'),
    ('Com', 'Computer Science'),
    ('Pol', 'Politics'),
    ('His', 'History'),
    ('Geo', 'Geography'),
    ('Psy', 'Psychology'),
    ('Fur', 'Further Maths'),
    ('Spa', 'Spanish'),
    ('PE', 'Physical Education'),
)

GRADE_CHOICES = (
    ('A*', 'A*'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


DATE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

MONTH_CHOICES = (
    ('Jan', '1'),
    ('Feb', '2'),
    ('Mar', '3'),
    ('Apr', '4'),
    ('May', '5'),
    ('Jun', '6'),
    ('Jul', '7'),
    ('Aug', '8'),
    ('Sep', '9'),
    ('Oct', '10'),
    ('Nov', '11'),
    ('Dec', '12'),
)

TEST_YEAR_CHOICES = (
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
)
    


class Tests(models.Model):
    test_subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    test_title = models.CharField(max_length=100)
    test_given_date= models.DateTimeField()
    date = models.CharField(max_length=4, choices=DATE_CHOICES)
    month = models.CharField(max_length=4, choices=MONTH_CHOICES)
    year = models.CharField(max_length=4, choices=TEST_YEAR_CHOICES)
    test_marks = models.DecimalField(decimal_places=0, max_digits=4, default=0)
    test_outof =  models.DecimalField(decimal_places=0, max_digits=4, default=0)
    #test_percentage = round(test_marks/test_outof)
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)