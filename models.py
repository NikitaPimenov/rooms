from django.db import models


class Building(models.Model):
    building_id = models.IntegerField(primary_key=True)
    name = models.CharField('Здание', max_length=10, default='')
    house = models.CharField('Корпус', max_length=10, default='')

    def __str__(self):
        return f'Здание {self.name}, Корпус {self.house}'

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    floor = models.IntegerField('Этаж', null=True)
    capacity = models.IntegerField('Количество мест', null=True)
    name = models.IntegerField('Номер комнаты', null=True)
    side = models.IntegerField(verbose_name='Сторона', default=0, choices=[
        (0, ''),
        (1, 'левая'),
        (2, 'правая')
    ])

    def calc_population(self):
        return len(self.profile_set.all())

    def __str__(self):
        s = ''
        if self.get_side_display() != '':
            s = ' ' + self.get_side_display()
        return f'Комната №{self.name}{s}, {self.building.name}, Корпус {self.building.house}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
