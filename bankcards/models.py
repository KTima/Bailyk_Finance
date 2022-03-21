from django.db import models
# Create your models here.

class TypeCard(models.Model):
    Type = models.CharField("Тип карты",max_length=250, unique=True )

    def __str__(self) :
        return self.Type

    class Meta:
        verbose_name = "Тип карты"
        verbose_name_plural = "Типы карт"

class SeriesCard(models.Model):
    Type = models.ForeignKey(TypeCard,verbose_name="Тип карты",on_delete=models.CASCADE)
    Series = models.CharField("Серия карты",max_length=250)

    def __str__(self) :
        return self.Series

    class Meta:
        verbose_name = "Серия карты"
        verbose_name_plural = "Серии карт"


class CardData(models.Model):
    status_choices = [
        ("не активирована", 'не активирована'),
        ("активирована", 'активирована'),
        ("просрочена", 'просрочена'),
    ]
    Series = models.ForeignKey(SeriesCard,verbose_name="Серия карты",on_delete=models.CASCADE)
    Numbers = models.BigIntegerField("Номер карты",default = 0,unique=True)
    Relase_date = models.DateTimeField("Дата выпуска карты",auto_now_add=True)
    End_date = models.DateTimeField("Дата окончания активности карты",blank = True,null=True)
    Use_date = models.DateTimeField("Дата использования",blank = True,null=True)
    Summ = models.IntegerField("Сумма",default=0)
    Status = models.CharField("Статус карты",max_length=100,choices=status_choices,default="не активирована")


    def __str__(self) :
        return str(self.Numbers)

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"


class HistoryCard(models.Model):
    Card = models.ForeignKey(CardData,verbose_name="Номер серии",on_delete=models.CASCADE)
    Use_date = models.DateTimeField("Дата покупки",auto_now_add=True)
    Summ = models.IntegerField("Сумма покупки",default=0)

    def __str__(self) :
        return str(self.Card)

    class Meta:
        verbose_name = "История карты"
        verbose_name_plural = "Истории карты"


class Create(models.Model):
    series_choices = [
        ("Visa", 'Visa'),
        ("MasterCard", 'MasterCard'),
    ]
    Series = models.CharField("Серия карты",choices=series_choices,max_length=250)
    kolvo = models.IntegerField("Колчество карт",default=0)
