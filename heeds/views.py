from django.shortcuts import render, redirect
import folium
import geocoder
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from .models import Search
from .forms import SearchForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = SearchForm()
    mapObj = ""
    datas = []
    lat = []
    lng = []
    country = []
    region = []
    location = []
    address = Search.objects.all()
    print(address)

    if len(address) != 0:
        addlast = address.last()
        for i in range(len(address)):
            location += geocoder.osm(address[i])

        for j in location:
            lat.append(j.lat)

            lng.append(j.lng)
            country.append(j.country)
            # city = location.city
            region.append(j.region)

        #print(location)
        #print(lat)
        #print(lng)
        print(region)

        if lat == None or lng == None:
            addlast.delete()
            return HttpResponseRedirect('/')

        # Create Map Object
        map = folium.Map(location=[19, -12], zoom_start=2)

        for data in range(len(address)):
            folium.Marker([lat[data], lng[data]], tooltip='Click for more',
                popup=[country[data], region[data]]).add_to(map)

        # Get HTML Represetation of Map Object
        mapObj = map._repr_html_()
    else:
        map = folium.Map(location=[19, -12], zoom_start=2)

        # Get HTML Represetation of Map Object
        mapObj = map._repr_html_()

    context ={
        'mapObj': mapObj,
        'form': form
    }
    return render(request, 'index.html', context)


def place(request):
    places = Search.objects.all()
    context = {
        'places': places,
    }
    return render(request, 'place.html', context)


def update(request, pk):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            up = Search.objects.get(id=pk)

            print('--------------------------------------')
            data = SearchForm(request.POST, instance=up)
            data.save()
            return HttpResponseRedirect('/place')
    else:
        form = SearchForm()

    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


def delete(request, pk):
    places = Search.objects.all()

    for place in places:
        print(place.id)
    if request.method == 'POST':
        up = Search.objects.filter(id=pk)

        up.delete()
        return HttpResponseRedirect('/place')
    else:
        form = SearchForm()


    context = {
        'place': place,
    }
    return render(request, 'delete.html', context)


