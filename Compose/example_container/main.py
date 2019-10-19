from flask import Flask, jsonify

app = Flask(__name__)

documentaries = [
    {
        "pk": "5b0fd5a0-6d2b-4de7-83d7-263cb6237d25",
        "title": "Saturn: Lord of The Rings",
        "slug": "saturn-lord-of-the-rings",
        "description": "With its famous rings, Saturn is the most distant planet clearly visible to the naked eye. But how did the rings get there and when were they formed? To study the planet in detail, scientists needed to get closer. So on 15 October 1997, the Cassini-Huygens spacecraft was launched.\nThe Cassini-Huygens is one of the most ambitious spacecraft ever launched, taking seven years to reach Saturn. The mission itself consists of two separate probes. The first is the enormous Cassini probe, designed to gather information about all aspects of the Saturnian system, from its many rings to its 33 moons. The second is the Huygens probe, a smaller wok-shaped craft, attached to the side of Cassini. Its task is to plunge through the atmosphere of Titan, Saturn’s largest and most mysterious moon.\nThe project is a joint NASA, European Space Agency (ESA) and Italian Space Agency venture. It has cost $3.27 billion and involves over 17 countries. It was inspired by another successful mission- the launch of the two Voyager Deep Space probes. These left Earth in 1977, and arrived separately at Saturn in 1980 and 1981. They sent back revolutionary data, changing what scientists thought about the Saturnian system.\nThey revealed that Saturn’s rings are far more complex and dynamic than any one had ever imagined. They also suggested that the rings had been formed after the planet itself. Why? And how old were they? But the Voyager probes had to move on, past Uranus and Neptune and beyond, leaving these fundamental questions about the rings unanswered.\n",
        "categories": ["Space", "Science"],
        "video": "https://www.youtube.com/embed/JtGsUd5E_wQ",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryaddict.com/films/the-universe-saturn-lord-of-the-rings",
                    "https://documentaryheaven.com/saturn-lord-of-the-rings/"]
    },
    {
        "pk": "355cb28e-03b9-4fdc-9774-60e226c5c670",
        "title": "Ross Kemp on Gangs – Jamaica (2007)",
        "slug": "ross-kemp-on-gangs-jamaica-2007",
        "description": "Highest murder rate in the world for a country not officially at war. Ross visits Kingston, the most violent area in all of Jamaica, and speaks to gang members there.\n“A study carried out by A. Harriott shows that the homicide rate in Jamaica is four times higher than the world rate, with the city of Kingston having the highest rate in the world at 109/100,000, followed by Washington D. More..C., at 67/100,000. According to this researcher, there is a direct relationship between the rate of murder and the rates of other violent crimes-robberies, rapes, etc. In Jamaica, historically, most murders were crimes of passion. In 1963, in 64% of the murder cases, the victims were known to the offender, and domestic violence accounted for 28% of all homicides, while in 1993, this declined to 16%. This does not mean that cases of domestic violence are on the decline, it means that the murder rate – especially since the increase in the number of illegal guns on the island – is going up.”\n",
        "categories": ["Drugs", "Lifestyle", "Gangs"],
        "video": "https://www.liveleak.com/ll_embed?f=a0e_1191860210",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/ross-kemp-on-gangs-jamaica/",
                    "https://documentaryheaven.com/ross-kemp-on-gangs-jamaica-2007/"]
    },
    {
        "pk": "41ff2de8-2c37-44f0-9ba8-09e3323eca37",
        "title": "Oil, Smoke and Mirrors",
        "slug": "oil-smoke-and-mirrors",
        "description": "Oil Smoke and Mirrors offers us a sobering critique of our perceived recent history, of our present global circumstances, and of our shared future in light of imminent, under-reported and mis-represented energy production constraints.\nThrough a series of impressively candid, informed and articulate interviews, this film argues that the bizarre events surrounding the 9/11 attacks, and the equally bizarre prosecution of the so-called war on terror, can be more credibly understood in the wider context of an imminent and critical divergence between available global oil supply and increasing global oil demand.\nThe picture Oil, Smoke & Mirrors paints is one of a tragically hyper-mediated global-political culture, which, for whatever reason, demonstrably disassociates itself from the values it claims to represent.\nWhile the ideas presented in this film can at first seem daunting, it's ultimate assertion is that these challenges can indeed be met and perhaps surpassed if, but only if, we can find first the courage to perceive them.",
        "categories": ["9/11", "Society", "News & Politics", "911", "Movies"],
        "video": "https://www.youtube.com/embed/oVzJhlvtDms",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/oil-smoke-and-mirrors/",
                    "https://documentaryaddict.com/films/oil-smoke-and-mirrors"]
    },
    {
        "pk": "fe4d516b-9ff2-41a2-9b2f-909067957f99",
        "title": "Ross Kemp: In Search of Pirates",
        "slug": "ross-kemp-in-search-of-pirates",
        "description": "The actor investigates the boom in piracy on the world’s oceans, traveling to some of the planet’s biggest trouble spots to discover the problems faced by potential targets and those trying to protect them.\nHe begins in London, where he discovers the economic impact of hijackings on global trade, before joining a Royal Navy anti-piracy ship in the Gulf of Aden off Somalia.\nThan he explores the impact of piracy in Nigeria, where more people are killed in raids than anywhere else in the world. He discovers the devastating effects that pirates are having on the area’s fishing fleet, with almost 300 workers killed over the past few years, and how attacks on oil tankers at the port of Lagos are threatening the country’s economy.\nEpisode 1: The actor investigates the boom in piracy on the world’s oceans, travelling to some of the planet’s biggest trouble spots to discover the problems faced by potential targets and those trying to protect them. He begins in London, where he discovers the economic impact of hijackings on global trade, before joining a Royal Navy anti-piracy ship in the Gulf of Aden off Somalia\nEpisode 2: The actor explores the impact of piracy in Nigeria, where more people are killed in raids than anywhere else in the world. He discovers the devastating effects that pirates are having on the area’s fishing fleet, with almost 300 workers killed over the past few years, and how attacks on oil tankers at the port of Lagos are threatening the country’s economy\n",
        "categories": ["Gangs", "News & Politics", "Lifestyle", "Crime", "Law"],
        "video": "https://www.youtube.com/embed/7U8WZE2lEa0",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/ross-kemp-in-search-of-pirates-ep3/",
                    "https://documentaryheaven.com/ross-kemp-in-search-of-pirates/"]
    },
    {
        "pk": "a113887f-d037-4774-a2ed-c767c0a0964c",
        "title": "Facing Goliath",
        "slug": "facing-goliath",
        "description": "The award winning and nationally broadcast documentary about Ray Taylor and his natural bodybuilding friend, Sebastian MacLean. When at age 50 Ray discovers that he is going blind, he is challenged by Sebastian to begin a journey of physical and emotional transformation. Facing Goliath follows Ray as he changes from a 232lb couch Potatoe into a competitive bodybuilder.\nCompeting in the world of bodybuilding together, Ray and Sebastian both discover what it means to face challenges that at first seem too big to handle. By facing giant challenges, these men find that a little faith and heart can change everything.\n",
        "categories": ["Health", "Sport", "Sport & Adventure"],
        "video": "https://www.youtube.com/embed/gijdyieuHi8",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryaddict.com/films/facing-goliath",
                    "https://documentaryheaven.com/facing-goliath/"]
    },
    {
        "pk": "73365bb2-5259-41b4-969e-f7dc094c6a51",
        "title": "In It’s Image",
        "slug": "in-its-image",
        "description": "In the mid 70s, an aspiring theoretical physicist made what he and many others feel is the most important discovery in the world. This very significant documentary is about the resulting invention, one that can author all subsequent ideas, provide a totally unanticipated cosmology, and possibly deliver us from death.\nThis is a blurb from the In Its Image Incorporated website…\nIn Its Image Incorporated is a California non-profit corporation that is literally dedicated to saving everyone’s lives. Its primary mission is to achieve life extension through the melding of human consciousness with a radically new kind of machine intelligence. Its secondary mission is to demonstrate the plausibility of achieving this profound purpose, and in so doing, fund the main objective of immortality.\n",
        "categories": ["Technology", "Science"],
        "video": "//player.vimeo.com/video/59193098",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/in-it%e2%80%99s-image/",
                    "https://documentaryheaven.com/in-its-image/"]
    },
    {
        "pk": "596c3150-09b6-4bb5-a63a-95775bafd1c3",
        "title": "Free For All",
        "slug": "free-for-all",
        "description": "Can we trust our elections? My name is John. Since I was a kid, I have been a proud American. But after questionable elections led to disastrous outcomes for my country, I felt I had to find out if our process of electing leaders was secure. This investigation led me on a journey throughout Ohio, the pivotal swing state that decided the last presidential election.  I met politicians, activists, election officials, journalists, attorneys, party leaders, a lot of cool locals who helped me shoot it all, and Jerry Springer.\nThe evidence I came across showed not just efforts to steal votes at the polls, but to systematically block millions of Americans from even casting a vote. When some people know they can’t win fairly, they’ll do everything they can to cheat.\nMy hope is that this will help everyone understand how our elections are really going down, left now in 2008, left here in America. Voting is not enough anymore. (though a huge turnout is key)As I found out, the 2008 election has already been stolen: We need to swipe it back.\n",
        "categories": ["News & Politics", "Conspiracy"],
        "video": "https://www.youtube.com/embed/--Db2kbs67M",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/free-for-all-2/",
                    "https://documentaryheaven.com/free-for-all/"]
    },
    {
        "pk": "0c8740aa-82be-4ab6-8ce5-c18c8b54c80b",
        "title": "Child Slavery",
        "slug": "child-slavery",
        "description": "In our society we take it for granted that children do not have to work or beg on streets, but according do this documentary there are still over 80 million kids in slavery worldwide. But how can it be, that child slavery is still existing? This documentary film shows how these young slaves live and what factors cause them to live under such conditions and who profits form this dirty business.\n",
        "categories": ["Human Rights", "Society"],
        "video": "https://www.youtube.com/embed/xmLCO3U7HsE",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/child-slavery-with-rageh-omaar/",
                    "https://documentaryheaven.com/child-slavery/"]
    },
    {
        "pk": "96d75302-f212-4123-8a02-e59a6176f2f7",
        "title": "The Phoenix Lights",
        "slug": "the-phoenix-lights",
        "description": "The Phoenix Lights (sometimes referred to as the \"lights over Phoenix\") were a series of widely sighted optical phenomena (generally unidentified flying objects) that occurred in the skies over the U.S. states of Arizona and Nevada, and the Mexican state of Sonora on March 13, 1997. A repeat of the lights occurred February 6, 2007, and was filmed by the local Fox News TV station.A similar incident occurred April 21, 2008. This incident was later revealed to be prank-flares attached to helium balloons.Lights of varying descriptions were seen by thousands of people between 19:30 and 22:30 MST, in a space of about 300 miles, from the Nevada line, through Phoenix, to the edge of Tucson. There were two distinct events involved in the incident: a triangular formation of lights seen to pass over the state, and a series of stationary lights seen in the Phoenix area.The United States Air Force (USAF) identified the second group of lights as flares dropped by A-10 Warthog aircraft which were on training exercises at the Barry Goldwater Range in southwest Arizona. Witnesses claim to have observed a huge carpenter's square-shaped UFO, containing lights or possibly light-emitting engines. Fife Symington, the governor at the time, was one witness to this incident. ",
        "categories": ["Mystery", "Space", "Conspiracy"],
        "video": "https://www.youtube.com/embed/UWCMPyLSlSo",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryheaven.com/the-phoenix-lights/",
                    "https://documentaryaddict.com/films/the-phoenix-lights-4101a357-8d51-4e1c-a324-1b5c08f2f4d4"]
    },
    {
        "pk": "ea812488-552f-4398-8e3f-370fadeb7ba5",
        "title": "9/11: The Road To Tyranny",
        "slug": "9-11-the-road-to-tyranny",
        "description": "The mainstream media is whitewashing and lying about what really happened on Sept 11th. 911: The Road to Tyranny is shaking the foundations of Washington, DC as the definitive film on what really happened on Sept. 11th and who stands to gain. The dark forces of Global Government are funding, training and protecting terrorist groups worldwide. In this blockbuster which has gained worldwide prestige you will learn the origins and the true story behind 9/11.\n",
        "categories": ["911", "9/11", "Conspiracy"],
        "video": "https://www.youtube.com/embed/OVMyH8eOHKs",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryaddict.com/films/9-11-the-road-to-tyranny",
                    "https://documentaryheaven.com/911-the-road-to-tyranny/"]
    },
    {
        "pk": "9366e692-1182-4706-bff3-cbb6537df795",
        "title": "Martial Law 9/11: The Rise of the Police State",
        "slug": "martial-law-9-11-the-rise-of-the-police-state",
        "description": "If you don’t know who Alex Jones is, you will never forget him after watching this ground-shaking documentary about the creeping police state in the United States.\nKnow that the north and south towers of the World Trade Center Complex were not the only two buildings to collapse that day? Did you know a third one collapsed hours after the collapses of the twin towers?\nHow did this third building collapse if it wasn’t hit by an airplane? Loose Change raises such questions and other blatant contradictions about the official 9/11 story fed to us by the government and media. By far one of the most comprehensive documentaries questioning what really happened on 9/11 and who should really be held accountable.\n",
        "categories": ["911", "9/11", "Activist", "News & Politics"],
        "video": "https://www.youtube.com/embed/uzo9IAgyOr0",
        "year": None,
        "duration": None,
        "sources": ["https://documentaryaddict.com/films/martial-law-9-11-the-rise-of-the-police-state",
        "https://documentaryheaven.com/martial-law-911-rise-of-police-state/"]
    }
]

@app.route('/')
def index():
    return jsonify(documentaries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)