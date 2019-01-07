from django.db import models

# Create your models here.
class Card(models.Model):
    # (e.g. SSR, R, N)
    rarity = models.ForeignKey('CardRarity', on_delete=models.SET_NULL)

    # (Highest rarity achieved e.g. SR, SR+, SRMAX [represented as int])
    max_level_reached = models.IntegerField(default=0)

    # Must be unique
    name = models.CharField(max_length=50, null=False, blank=True, unique=True)

    # CARD_RARITY_CHOICES = ( // Might not be viable if there are different card raritys
    #     ('N' , 'Normal'),
    #     ('R' , 'Rare'),
    #     ('SR' , 'Super Rare'),
    #     ('SSR' , 'Super Super Rare'),
    #     ('GR' , 'Great Rare'),
    #     ('LR' , 'Legend'),
    #     ('SLR' , 'Super Legend'), 
    # )

    # def validate_uniqueness(self):
    #     if (Card.objects.filter(name=self.name).exists()):
    #         # Raise error if Name/Label pair are not completely unique
    #         raise ValidationError('Name and Label must be unique')

    # def save(self, *args, **kwargs):
    #     self.validate_uniqueness()
    #     super(Card, self).save(*args, **kwargs)


class CardRarity(models.Model):
    # Starts from 0 (SR) to 4 (SRMAX) [Note: Rarities can have different max levels]
    max_level = models.IntegerField()

    # Actual value that appears ("SR", "R", "N")
    label = models.CharField(max_length=4, null=False, blank=False, unique=True)

    # Full name of label ("Super Rare", "Rare", "Normal")
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)

    # RARITY_CHOICES return (RarityLabel, RarityName)
    @classmethod
    def choices(cls):
        # List of all rarities here
        rarity_set = cls.objects.all()
        choice_list = []

        for item in rarity_set:
            choice_list.push((item.label, item.name))
        
        return tuple(choice_list)

    # def validate_uniqueness(self):
    #     if (CardRarity.objects.filter(name=self.name).exists() or
    #         CardRarity.objects.filter(label=self.label).exists()):
    #         # Raise error if Name/Label pair are not completely unique
    #         raise ValidationError('Name and Label must be unique')

    # def save(self, *args, **kwargs):
    #     self.validate_uniqueness()
    #     super(CardRarity, self).save(*args, **kwargs)
