import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Iso, Region


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()

#---------
# Cultural Landscape and Archaeological Remains of the Bamiyan Valley
# ---------
# <p>The cultural landscape and archaeological remains of the Bamiyan Valley represent the artistic and religious developments which from the 1st to the 13th centuries characterized ancient Bakhtria, integrating various cultural influences into the Gandhara school of Buddhist art. The area contains numerous Buddhist monastic ensembles and sanctuaries, as well as fortified edifices from the Islamic period. The site is also testimony to the tragic destruction by the Taliban of the two standing Buddha statues, which shook the world in March 2001.</p>
# ---------
# <p><em>Criterion (i):</em> The Buddha statues and the cave art in Bamiyan Valley are an outstanding representation of the Gandharan school in Buddhist art in the Central Asian region.</p> <p><em>Criterion (ii)</em> : The artistic and architectural remains of Bamiyan Valley, and an important Buddhist centre on the Silk Road, are an exceptional testimony to the interchange of Indian, Hellenistic, Roman, Sasanian influences as the basis for the development of a particular artistic expression in the Gandharan school. To this can be added the Islamic influence in a later period.</p> <p><em>Criterion (iii):</em> The Bamiyan Valley bears an exceptional testimony to a cultural tradition in the Central Asian region, which has disappeared.</p> <p><em>Criterion (iv):</em> The Bamiyan Valley is an outstanding example of a cultural landscape which illustrates a significant period in Buddhism.</p> <p><em>Criterion (vi):</em> The Bamiyan Valley is the most monumental expression of the western Buddhism. It was an important centre of pilgrimage over many centuries. Due to their symbolic values, the monuments have suffered at different times of their existence, including the deliberate destruction in 2001, which shook the whole world.</p>
# ---------
# 2003
# ---------
# 67.82525
# ---------
# 34.84694
# ---------
# 158.9265
# ---------
# Cultural
# ---------
# Afghanistan
# ---------
# Asia and the Pacific
# ---------
# af


# name_0,description_1,justification_2,year_3,longitude_4,latitude_5,area_hectares_6,category_7,state_8,region_9,iso_10

    # for row in reader:
    #     for ele in row:
    #         print('---------')
    #         print(ele)
    #     break

        # p, created = Person.objects.get_or_create(email=row[0])
        # c, created = Course.objects.get_or_create(title=row[2])

        # r = Membership.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()

    for row in reader:
        category, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        iso, created = Iso.objects.get_or_create(name=row[10])
        region, created = Region.objects.get_or_create(name=row[9])

        try:
            year=int(row[3])
        except:
            year=None

        try:
            latitude=float(row[5])
        except:
            latitude=None
        
        try:
            longitude=float(row[4])
        except:
            longitude=None

        try:
            area_hectares=float(row[6])
        except:
            area_hectares=None

        site = Site(name=row[0],
                    description=row[1],
                    justification=row[2],
                    year=year,
                    longitude=longitude,
                    latitude=latitude,
                    area_hectares=area_hectares,
                    category=category,
                    state=state,
                    region=region,
                    iso=iso)
        site.save()

        # name_0,description_1,justification_2,year_3,longitude_4,latitude_5,area_hectares_6,category_7,state_8,region_9,iso_10