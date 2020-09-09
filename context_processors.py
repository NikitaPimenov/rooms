from .models import Building


def building_list(request):
    return {
        "building_list": Building.objects.order_by('-name')
    }
