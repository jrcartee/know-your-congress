from django.db import models


class Bill(models.Model):
    PREFIXES = (
        ('S', "Senate - Bill"),
        ('H.R.', "House of Reps - Bill"),
        ('S.J.Res.', "Senate - Joint Resolution"),
        ('H.J.Res.', "House of Reps - Joint Resolution"),
        ('S.Con.Res.', "Senate - Concurrent Resolution"),
        ('H.Con.Res.', "House of Reps - Concurrent Resolution"),
        ('S.Res.', "Senate - Simple Resolution"),
        ('H.Res.', "House of Reps - Simple Resolution"),
    )
    prefix = models.CharField(max_length=10, choices=PREFIXES)
    number = models.PositiveSmallIntegerField()
    congress = models.PositiveSmallIntegerField()

    sponser = models.ForeignKey('people.Legislator')
    title = models.TextField()
    public = models.BooleanField()

    status = models.OneToOneField('Action')

    start = models.DateField()
    # only for enacted bills
    law_num = models.PositiveSmallIntegerField(null=True)
    law_public = models.BooleanField(null=True)


class Action(models.Model):
    ACTION_TYPES = (
        ('A', "Ammendment"),
        ('P', "Passage"),
        ('O', "Other")
    )
    CHAMBERS = (
        ('S', "Senate"),
        ('R', "House of Representatives")
    )
    bill = models.ForeignKey(Bill)
    atype = models.CharField(max_length=1, choices=ACTION_TYPES)
    chamber = models.CharField(max_length=1, choices=CHAMBERS)
    proposal = models.TextField(null=True, blank=True)

    total_for = models.PositiveSmallIntegerField()
    total_against = models.PositiveSmallIntegerField()
    total_other = models.PositiveSmallIntegerField()


class Vote(models.Model):
    action = models.ForeignKey(Action)
    person = models.ForeignKey('people.Legislator')
    vote = models.BooleanField(null=True, blank=True)
