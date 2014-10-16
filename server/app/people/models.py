from django.db import models


class Role(models.Model):
    person = models.ForeignKey('Legislator', related_name="roles")
    PARTIES = (
        ('R', "Republican"),
        ('D', "Democrat"),
        ('I', "Independent")
    )
    party = models.CharField(max_length=1, choices=PARTIES)
    TYPES = (
        ('S', "Senator"),
        ('R', "Representative")
    )
    role_type = models.CharField(max_length=1, choices=TYPES)

    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=12)
    website = models.URLField()
    current = models.BooleanField()
    start = models.DateField()
    end = models.DateField(null=True)

    _extra = models.PositiveSmallIntegerField(db_column='extra')

    @property
    def sen_class(self):
        """ senators serve a 6 yr total term
            classes are 2 yr segments of the total term
        """
        if self.role == 'S':
            return self._extra

    @sen_class.setter
    def sen_class(self, value):
        if value in range(1, 4):
            self._extra = value
        else:
            raise AttributeError("Senators must be 1 of 3 classes")

    @property
    def district(self):
        """ district # being represented by this person
            numbered on a per-state basis
        """
        if self.role == 'R':
            return self._extra

    @district.setter
    def district(self, value):
        self._extra = value


class Legislator(models.Model):
    first = models.CharField(max_length=20)
    middle = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    birth = models.DateField()
    twitter = models.CharField(max_length=40)
    youtube = models.CharField(max_length=40)

    def full_name(self):
        name = self.first
        if self.middle:
            name += " " + self.middle
        name += " " + self.last
        return name


class Committee(models.Model):
    CHAMBERS = (
        ('S', "Senate"),
        ('R', "House of Representatives")
    )
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)

    chamber = models.CharField(max_length=1, choices=CHAMBERS)
    members = models.ManyToManyField(Legislator, related_name='committees')
