from flask import Blueprint, render_template
import os

views = Blueprint('views', __name__)


@views.route('/')
def home():
    info = [
        {
            "state": "Alabama",
            "capital": "Montgomery"
        },
        {
            "state": "Alaska",
            "capital": "Juneau"
        },
        {
            "state": "Arizona",
            "capital": "Phoenix"
        },
        {
            "state": "Arkansas",
            "capital": "Little Rock"
        },
        {
            "state": "California",
            "capital": "Sacramento"
        },
        {
            "state": "Colorado",
            "capital": "Denver"
        },
        {
            "state": "Connecticut",
            "capital": "Hartford"
        },
        {
            "state": "Delaware",
            "capital": "Dover"
        },
        {
            "state": "Florida",
            "capital": "Tallahassee"
        },
        {
            "state": "Georgia",
            "capital": "Atlanta"
        },
        {
            "state": "Hawaii",
            "capital": "Honolulu"
        },
        {
            "state": "Idaho",
            "capital": "Boise"
        },
        {
            "state": "Illinois",
            "capital": "Springfield"
        },
        {
            "state": "Indiana",
            "capital": "Indianapolis"
        },
        {
            "state": "Iowa",
            "capital": "Des Moines"
        },
        {
            "state": "Kansas",
            "capital": "Topeka"
        },
        {
            "state": "Kentucky",
            "capital": "Frankfort"
        },
        {
            "state": "Louisiana",
            "capital": "Baton Rouge"
        },
        {
            "state": "Maine",
            "capital": "Augusta"
        },
        {
            "state": "Maryland",
            "capital": "Annapolis"
        },
        {
            "state": "Massachusetts",
            "capital": "Boston"
        },
        {
            "state": "Michigan",
            "capital": "Lansing"
        },
        {
            "state": "Minnesota",
            "capital": "Saint Paul"
        },
        {
            "state": "Mississippi",
            "capital": "Jackson"
        },
        {
            "state": "Missouri",
            "capital": "Jefferson City"
        },
        {
            "state": "Montana",
            "capital": "Helena"
        },
        {
            "state": "Nebraska",
            "capital": "Lincoln"
        },
        {
            "state": "Nevada",
            "capital": "Carson City"
        },
        {
            "state": "New Hampshire",
            "capital": "Concord"
        },
        {
            "state": "New Jersey",
            "capital": "Trenton"
        },
        {
            "state": "New Mexico",
            "capital": "Santa Fe"
        },
        {
            "state": "New York",
            "capital": "Albany"
        },
        {
            "state": "North Carolina",
            "capital": "Raleigh"
        },
        {
            "state": "North Dakota",
            "capital": "Bismarck"
        },
        {
            "state": "Ohio",
            "capital": "Columbus"
        },
        {
            "state": "Oklahoma",
            "capital": "Oklahoma City"
        },
        {
            "state": "Oregon",
            "capital": "Salem"
        },
        {
            "state": "Pennsylvania",
            "capital": "Harrisburg"
        },
        {
            "state": "Rhode Island",
            "capital": "Providence"
        },
        {
            "state": "South Carolina",
            "capital": "Columbia"
        },
        {
            "state": "South Dakota",
            "capital": "Pierre"
        },
        {
            "state": "Tennessee",
            "capital": "Nashville"
        },
        {
            "state": "Texas",
            "capital": "Austin"
        },
        {
            "state": "Utah",
            "capital": "Salt Lake City"
        },
        {
            "state": "Vermont",
            "capital": "Montpelier"
        },
        {
            "state": "Virginia",
            "capital": "Richmond"
        },
        {
            "state": "West Virginia",
            "capital": "Charleston"
        },
        {
            "state": "Wisconsin",
            "capital": "Madison"
        },
        {
            "state": "Wyoming",
            "capital": "Cheyenne"
        }
    ]

    return render_template("home.html", info=info)


@views.route('/<capital>/')
def state_capital(capital):
    capital = capital.title()

    states_and_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Monies',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }

    weather_links = {
        'Montgomery': "https://forecast7.com/en/32d37n86d30/montgomery/?unit=us",
        'Juneau': "https://forecast7.com/en/58d30n134d42/juneau/?unit=us",
        'Phoenix': "https://forecast7.com/en/33d45n112d07/phoenix/?unit=us",
        'Little Rock': "https://forecast7.com/en/34d75n92d29/little-rock/?unit=us",
        'Sacramento': "https://forecast7.com/en/38d58n121d49/sacramento/?unit=us",
        'Denver': "https://forecast7.com/en/39d74n104d99/denver/?unit=us",
        'Hartford': "https://forecast7.com/en/41d76n72d69/hartford/?unit=us",
        'Dover': "https://forecast7.com/en/39d16n75d52/dover/?unit=us",
        'Tallahassee': "https://forecast7.com/en/30d44n84d28/tallahassee/?unit=us",
        'Atlanta': "https://forecast7.com/en/33d75n84d39/atlanta/?unit=us",
        'Honolulu': "https://forecast7.com/en/21d31n157d86/honolulu/?unit=us",
        'Boise': "https://forecast7.com/en/43d62n116d21/boise/?unit=us",
        'Springfield': "https://forecast7.com/en/39d78n89d65/springfield/?unit=us",
        'Indianapolis': "https://forecast7.com/en/39d77n86d16/indianapolis/?unit=us",
        'Des Monies': "https://forecast7.com/en/41d60n93d61/des-moines/?unit=us",
        'Topeka': "https://forecast7.com/en/39d06n95d69/topeka/?unit=us",
        'Frankfort': "https://forecast7.com/en/39d06n95d69/topeka/?unit=us",
        'Baton Rouge': "https://forecast7.com/en/30d46n91d14/baton-rouge/?unit=us",
        'Augusta': "https://forecast7.com/en/44d31n69d78/augusta/?unit=us",
        'Annapolis': "https://forecast7.com/en/38d98n76d49/annapolis/?unit=us",
        'Boston': "https://forecast7.com/en/42d36n71d06/boston/?unit=us",
        'Lansing': "https://forecast7.com/en/42d73n84d56/lansing/?unit=us",
        'Saint Paul': "https://forecast7.com/en/44d95n93d09/saint-paul/?unit=us",
        'Jackson': "https://forecast7.com/en/32d30n90d18/jackson/?unit=us",
        'Jefferson City': "https://forecast7.com/en/38d58n92d17/jefferson-city/?unit=us",
        'Helena': "https://forecast7.com/en/46d59n112d02/helena/?unit=us",
        'Lincoln': "https://forecast7.com/en/40d83n96d69/lincoln/?unit=us",
        'Carson City': "https://forecast7.com/en/39d16n119d77/carson-city/?unit=us",
        'Concord': "https://forecast7.com/en/43d21n71d54/concord/?unit=us",
        'Trenton': "https://forecast7.com/en/40d22n74d74/trenton/?unit=us",
        'Santa Fe': "https://forecast7.com/en/35d69n105d94/santa-fe/?unit=us",
        'Albany': "https://forecast7.com/en/42d65n73d76/albany/?unit=us",
        'Raleigh': "https://forecast7.com/en/35d78n78d64/raleigh/?unit=us",
        'Bismarck': "https://forecast7.com/en/46d81n100d78/bismarck/?unit=us",
        'Columbus': "https://forecast7.com/en/39d96n83d00/columbus/?unit=us",
        'Oklahoma City': "https://forecast7.com/en/35d47n97d52/oklahoma-city/?unit=us",
        'Salem': "https://forecast7.com/en/44d94n123d04/salem/?unit=us",
        'Harrisburg': "https://forecast7.com/en/40d27n76d89/harrisburg/?unit=us",
        'Providence': "https://forecast7.com/en/41d82n71d41/providence/?unit=us",
        'Columbia': "https://forecast7.com/en/34d00n81d03/columbia/?unit=us",
        'Pierre': "https://forecast7.com/en/44d37n100d35/pierre/?unit=us",
        'Nashville': "https://forecast7.com/en/36d16n86d78/nashville/?unit=us",
        'Austin': "https://forecast7.com/en/30d27n97d74/austin/?unit=us",
        'Salt Lake City': "https://forecast7.com/en/40d76n111d89/salt-lake-city/?unit=us",
        'Montpelier': "https://forecast7.com/en/44d26n72d58/montpelier/?unit=us",
        'Richmond': "https://forecast7.com/en/37d54n77d44/richmond/?unit=us",
        'Olympia': "https://forecast7.com/en/47d04n122d90/olympia/?unit=us",
        'Charleston': "https://forecast7.com/en/38d35n81d63/charleston/?unit=us",
        'Madison': "https://forecast7.com/en/43d07n89d40/madison/?unit=us",
        'Cheyenne': '"https://forecast7.com/en/41d14n104d82/cheyenne/?unit=us"'
    }

    resources = {
        'Montgomery': "https://www.montgomeryal.gov/",
        'Juneau': "https://juneau.org/",
        'Phoenix': "https://www.phoenix.gov/",
        'Little Rock': "https://www.littlerock.gov/",
        'Sacramento': "https://www.cityofsacramento.org/",
        'Denver': "https://www.denvergov.org/",
        'Hartford': "https://www.hartfordct.gov/Home",
        'Dover': "https://www.dover.nh.gov/",
        'Tallahassee': "https://talgov.com/Main/Home.aspx",
        'Atlanta': "https://www.atlantaga.gov/",
        'Honolulu': "https://www.honolulu.gov/",
        'Boise': "https://www.cityofboise.org/",
        'Springfield': "https://www.springfield.il.us/",
        'Indianapolis': "https://www.indy.gov/",
        'Des Monies': "https://www.dsm.city/",
        'Topeka': "https://www.topeka.org/",
        'Frankfort': "https://frankfort.ky.gov/",
        'Baton Rouge': "https://www.brla.gov/",
        'Augusta': "https://www.augustamaine.gov/",
        'Annapolis': "https://www.annapolis.gov/",
        'Boston': "https://www.boston.gov/",
        'Lansing': "https://www.lansingmi.gov/",
        'Saint Paul': "https://www.stpaul.gov/",
        'Jackson': "https://www.jacksonms.gov/",
        'Jefferson City': "https://www.jeffersoncitymo.gov/",
        'Helena': "https://www.helenamt.gov/home",
        'Lincoln': "https://www.lincoln.ne.gov/Home",
        'Carson City': "https://www.carson.org/",
        'Concord': "https://www.concordnh.gov/",
        'Trenton': "https://www.trentonnj.org/",
        'Santa Fe': "https://www.santafenm.gov/",
        'Albany': "https://www.albanyny.gov/",
        'Raleigh': "https://raleighnc.gov/",
        'Bismarck': "https://www.bismarcknd.gov/",
        'Columbus': "https://www.columbus.gov/",
        'Oklahoma City': "https://www.okc.gov/",
        'Salem': "https://www.cityofsalem.net/",
        'Harrisburg': "https://harrisburgpa.gov/",
        'Providence': "https://www.providenceri.gov/",
        'Columbia': "https://columbiasc.gov/",
        'Pierre': "https://www.cityofpierre.org/",
        'Nashville': "https://www.nashville.gov/",
        'Austin': "https://www.austintexas.gov/",
        'Salt Lake City': "https://www.slc.gov/",
        'Montpelier': "https://montpelier.id.gov/",
        'Richmond': "https://www.rva.gov/",
        'Olympia': "https://www.olympiawa.gov/",
        'Charleston': "https://www.charlestonwv.gov/",
        'Madison': "https://www.cityofmadison.com/",
        'Cheyenne': "https://www.cheyennecity.org/Home"
    }

    weather = weather_links[capital]
    gov_site = resources[capital]

    for key, value in states_and_capitals.items():
        if capital == value:
            state = key

    pic = f"{capital}.png"

    return render_template("capital.html", capital=capital, state=state, weather=weather, gov_site=gov_site, pic=pic)
