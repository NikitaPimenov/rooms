from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Building, Room
from .filters import RoomFilter
from .forms import RoomForm, BuildingForm
from django.contrib.auth.models import User


@login_required
def list(request, building_id):
    building = get_object_or_404(Building, pk=building_id)
    context = {
        'rooms_list': building.room_set.all(),
        'building': building,
        'filter': RoomFilter(request.GET, queryset=building.room_set.all())
    }
    return render(request, 'rooms/list.html', context)


@login_required
def detail(request, building_id, room_id):
    room = get_object_or_404(Room, pk=room_id)
    usern = request.GET.get('Выселить')
    if usern:
        user = User.objects.filter(username=usern).first()
        if user:
            print(user.profile.patronymic)
            user.profile.room_id = None
            user.profile.save()
    return render(request, 'rooms/detail.html', context={
        'room': room
    })


@user_passes_test(lambda u: u.is_superuser)
def admin_del_room(request, pk):
    r = Room.objects.get(pk=pk)
    msg = f'{r} успешно удалена!'
    if r:
        r.delete()
    buildings = Building.objects.all().order_by('name', 'house')
    return render(request, 'rooms/administration.html', context={
        'buildings': buildings,
        'msg': msg
    })


@user_passes_test(lambda u: u.is_superuser)
def admin_add_stuff(request):
    buildings = Building.objects.all().order_by('name', 'house')
    return render(request, 'rooms/administration.html', context={
        'buildings': buildings
    })


@user_passes_test(lambda u: u.is_superuser)
def admin_add_room(request):
    form = RoomForm()
    return render(request, 'rooms/add.html', context={
        'form': form
    })


@user_passes_test(lambda u: u.is_superuser)
def admin_add_building(request):
    form = BuildingForm()
    return render(request, 'rooms/add.html', context={
        'form': form
    })


@user_passes_test(lambda u: u.is_superuser)
def add_accept(request):
    pk, form, msg = None, None, None
    if 'floor' in request.POST:
        form = RoomForm(request.POST)
        msg = 'Комната успешно добавлена!'
        rooms = Room.objects.order_by('-room_id')
        pk = rooms[0].pk + 1 if rooms else 1
    else:
        form = BuildingForm(request.POST)
        msg = 'Здание успешно добавлено!'
        buildings = Building.objects.order_by('-building_id')
        pk = buildings[0].pk + 1 if buildings else 1
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.pk = pk
        new_obj.save()
    else:
        return redirect('rooms:add_room')
    buildings = Building.objects.all().order_by('name', 'house')
    return render(request, 'rooms/administration.html', context={
        'buildings': buildings,
        'msg': msg
    })


@user_passes_test(lambda u: u.is_superuser)
def admin_alter(request, pk):
    building = Building.objects.get(pk=pk)
    rooms = building.room_set.all().order_by('floor', 'name', 'side')
    return render(request, 'rooms/alter_page.html', context={
        'building': building,
        'rooms': rooms
    })


@user_passes_test(lambda u: u.is_superuser)
def alter_room(request, pk):
    room = Room.objects.get(pk=pk)
    form = RoomForm(instance=room)
    return render(request, 'rooms/alter.html', context={
        'pk': room.pk,
        'form': form
    })


@user_passes_test(lambda u: u.is_superuser)
def alter_building(request, pk):
    building = Building.objects.get(pk=pk)
    form = BuildingForm(instance=building)
    return render(request, 'rooms/alter.html', context={
        'pk': building.pk,
        'form': form
    })


@user_passes_test(lambda u: u.is_superuser)
def alter_accept(request, pk):
    form = msg = obj = outpk = None
    if 'floor' in request.POST:
        form = RoomForm(request.POST)
        obj = Room.objects.get(pk=pk)
        msg = 'Комната успешно изменена!'
        outpk = obj.building.pk
    else:
        form = BuildingForm(request.POST)
        msg = 'Здание успешно изменено!'
        obj = Building.objects.get(pk=pk)
        outpk = obj.pk
    if form.is_valid():
        obj = form.save(commit=False)
        obj.pk = pk
        obj.save()
    else:
        return redirect('rooms:alter_page', pk=outpk)
    building = Building.objects.get(pk=outpk)
    rooms = building.room_set.all().order_by('floor', 'name', 'side')
    return render(request, 'rooms/alter_page.html', context={
        'building': building,
        'rooms': rooms,
        'msg': msg
    })

# def move(request, building_id, room_id):
#    room = get_object_or_404(Room, pk=room_id)
#    return render(request, 'rooms/move.html', {'room': room})
