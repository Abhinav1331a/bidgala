account_type = {

	'Buyer' : 'b',
	'Seller' : 's',
	'Buyer & Seller' : 'both',
	'Buying for client' : 'pro'
}


# dim_measurement = {
# 	'Meter' : 'm',
# 	'Centimeter' : 'cm',
# 	'Inches' : 'i'
# }

 
professions = {
	'id' : 'Interior Designer',
	'hs' : 'Home Stager',
	'rsp' : 'Real Estate Professional',
	'ot' : 'Other'
}

TAGS = {
	'b' : 'BUYER',
	's' : 'SELLER',
	'both' : 'BOTH',
	'pro' : 'PROFESSIONAL',
}

# styles = {
# 	'abstract':'Abstract',
# 	'contemporary':'Contemporary',
# 	'figurative':'Figurative',
# 	'minimalist':'Minimalist',
# 	'portraiture':'Portraiture',
# 	'landscape':'Landscape',
# 	'fashion':'Fashion',
# 	'popart':'Pop Art',
# 	'other' : 'Other'	
# }

# material = {
# 	'canvas' : 'Canvas',
# 	'paper' : 'Paper',
# 	'wood' : 'Wood',
# 	'cardboard' : 'Cardboard',
# 	'soft' : 'Soft (Yam, Cotton, Fabric)',
# 	'plastic' : 'Plastic',
# 	'aluminum' : 'Aluminum',
# 	'glass' : 'Glass',
# 	'carbonfibre': 'Carbon Fibre',
# 	'steel' : 'Steel',
# 	'iron' : 'Iron',
# 	'bronze' : 'Bronze',
# 	'ceramic' : 'Ceramic',
# 	'stone' : 'Stone',
# 	'stainlesssteel' : 'Stainless Steel',
# 	'marble' : 'Marble',
# 	'other' : 'Other',

# }

# sub_type_one = {
# 	'abstract' : 'Abstract',
# 	'animalsBirdsFish' : 'Animals, Birds & Fish',
# 	'astronomySpace' : 'Astronomy & Space',
# 	'buildingsArchitecture' : 'Buildings & Architecture',
# 	'childrensArt' : "Children's Art",
# 	'entertainment' : 'Entertainment',
# 	'ethnicCulturalTribal' : 'Ethnic, Cultural & Tribal',
# 	'fantasyMythology' : 'Fantasy & Mythology',
# 	'flowersPlantsTrees' : 'Flowers, Plants & Trees',
# 	'foodBeverage' : 'Food & Beverage',
# 	'holidaysOccasions' : 'Holidays & Occasions',
# 	'humorSatire' : 'Humor & Satire',
# 	'landscapesNature' : 'Landscapes & Nature',
# 	'peopleFigures' : 'People & Figures',
# 	'placesTravel' : 'Places & Travel',
# 	'politicsPatriotism' : 'Politics & Patriotism',
# 	'religionPhilosophyAstrology' : 'Religion, Philosophy & Astrology',
# 	'scienceTechnology' : 'Science & Technology',
# 	'sportsHobbies' : 'Sports & Hobbies',
# 	'stillLife': 'Still Life',
# 	'vehiclesTransportation' : 'Vehicles & Transportation'
# }


# sub_type_two = {
	
# 	'bowlsPots': 'Bowls & Pots',
# 	'candleHolders': 'Candle Holders',
# 	'childrensArt': "Children's Art",
# 	'cupsGoblets': 'Cups Goblets',
# 	'figurative': 'Figurative',
# 	'fountainsWaterwalls': 'Fountains & Waterwalls',
# 	'jars': 'Jars',
# 	'jewelry': 'Jewelry',
# 	'masks': 'Masks',
# 	'mugsTankards': 'Mugs & Tankards',
# 	'ornaments': 'Ornaments',
# 	'pitchersJugs': 'Pitchers & Jugs',
# 	'platesSaucers': 'Plates & Saucers',
# 	'plattersTrays': 'Platters & Trays',
# 	'saltPepperShakers': 'Salt & Pepper Shakers',
# 	'sculpturalArtistic': 'Sculptural & Artistic',
# 	'teapotsSets': 'Teapots & Sets',
# 	'tiles': 'Tiles',
# 	'vasesUrns': 'Vases & Urns',
# 	'otherCeramics': 'Other Ceramics'

# }

# category = {
# 	'paintings' : 'Paintings',
# 	'prints' : 'Prints',
# 	'drawingIllustration' : 'Drawing & Illustration',
# 	'photography' : 'Photography',
# 	'sculptures' : 'Sculptures',
# 	'mixedMedia' : 'Mixed Media'
	
# }

# category_sell = {
# 	'paintings' : 'Paintings',
# 	'prints' : 'Prints',
# 	'drawingIllustration' : 'Drawing & Illustration',
# 	'photography' : 'Photography',
# 	'sculptures' : 'Sculptures',
# 	'ceramicPottery' : 'Ceramic & Pottery',
# 	'glass' : 'Glass',
	
	
# }


# subcategory = {
	
	
# 	'glass' : sub_type_two,
# 	'sculptures' : sub_type_one,
# 	'ceramicPottery' : sub_type_two,
# 	'photography' : sub_type_one,
# 	'drawingIllustration' : sub_type_one,
# 	'paintings' : sub_type_one,
# 	'prints' : sub_type_one
# }


# If any changes are made here, then also make chnages in profileupdate
country = {
	'CA' : {
		'name' : 'Canada',
		'states' : {
			'AB' : 'Alberta',
			'BC' : 'British Columbia',
			'MB' : 'Manitoba',
			'NB' : 'New Brunswick',
			'NL' : 'Newfoundland and Labrador',
			'NS' : 'Nova Scotia',
			'ON' : 'Ontario',
			'QC' : 'Quebec',
			'SK' : 'Saskatchewan',
			'YT' : 'Yukon',
			'NU' : 'Nunavut',
			'NT' : 'Northwest Territories'

		}
	},

	'US' : {
		'name' : 'US',
		'states' : {
			'AL' : 'Alabama',
			'AK' : 'Alaska',
			'AZ' : 'Arizona',
			'AR' : 'Arkansas',
			'CA' : 'California',
			'CO' : 'Colorado',
			'CT' : 'Connecticut',
			'DE' : 'Delaware',
			'DC' : 'District Of Columbia',
			'FL' : 'Florida',
			'GA' : 'Georgia',
			'HI' : 'Hawaii',
			'ID' : 'Idaho',
			'IL' : 'Illinois',
			'IN' : 'Indiana',
			'IA' : 'Iowa',
			'KS' : 'Kansas',
			'KY' : 'Kentucky',
			'LA' : 'Louisiana',
			'ME' : 'Maine',
			'MD' : 'Maryland',
			'MA' : 'Massachusetts',
			'MI' : 'Michigan',
			'MN' : 'Minnesota',
			'MS' : 'Mississippi',
			'MO' : 'Missouri',
			'MT' : 'Montana',
			'NE' : 'Nebraska',
			'NV' : 'Nevada',
			'NH' : 'New Hampshire',
			'NJ' : 'New Jersey',
			'NM' : 'New Mexico',
			'NY' : 'New York',
			'NC' : 'North Carolina',
			'ND' : 'North Dakota',
			'OH' : 'Ohio',
			'OK' : 'Oklahoma',
			'OR' : 'Oregon',
			'PA' : 'Pennsylvania',
			'RI' : 'Rhode Island',
			'SC' : 'South Carolina',
			'SD' : 'South Dakota',
			'TN' : 'Tennessee',
			'TX' : 'Texas',
			'UT' : 'Utah',
			'VT' : 'Vermont',
			'VA' : 'Virginia',
			'WA' : 'Washington',
			'WV' : 'West Virginia',
			'WI' : 'Wisconsin',
			'WY' : 'Wyoming'
		}
	},

	'IND' : {
		'name' : 'India',
		'states' : {
		    'AN':'Andaman and Nicobar Islands',
		    'AP':'Andhra Pradesh',
		    'AR':'Arunachal Pradesh',
		    'AS':'Assam',
		    'BR':'Bihar',
		    'CG':'Chandigarh',
		    'CH':'Chhattisgarh',
		    'DN':'Dadra and Nagar Haveli',
		    'DD':'Daman and Diu',
		    'DL':'Delhi',
		    'GA':'Goa',
		    'GJ':'Gujarat',
		    'HR':'Haryana',
		    'HP':'Himachal Pradesh',
		    'JK':'Jammu and Kashmir',
		    'JH':'Jharkhand',
		    'KA':'Karnataka',
		    'KL':'Kerala',
		    'LA':'Ladakh',
		    'LD':'Lakshadweep',
		    'MP':'Madhya Pradesh',
		    'MH':'Maharashtra',
		    'MN':'Manipur',
		    'ML':'Meghalaya',
		    'MZ':'Mizoram',
		    'NL':'Nagaland',
		    'OR':'Odisha',
		    'PY':'Puducherry',
		    'PB':'Punjab',
		    'RJ':'Rajasthan',
		    'SK':'Sikkim',
		    'TN':'Tamil Nadu',
		    'TS':'Telangana',
		    'TR':'Tripura',
		    'UP':'Uttar Pradesh',
		    'UK':'Uttarakhand',
		    'WB':'West Bengal'
	},

},

	'AU' : {
			'name' : 'Australia',
			'states' : {
				'NSW' : 'New South Wales',
				'VIC' : 'Victoria',
				'QLD' : 'Queensland',
				'TAS' : 'Tasmania',
				'SA' : 'South Australia',
				'WA' : 'Western Australia',
				'NT' : 'Northern Territory',
				'ACT' : 'Australian Capital Territory'
			}
		},
	
	'I' : {
		'name' : 'Italy',
		'states' : {
			'AG' : 'Agrigento',
			'AL' : 'Alessandria',
			'AN' : 'Ancona',
			'AO' : 'Aosta',
			'AR' : 'Arezzo',
			'AP' : 'Ascoli Piceno',
			'AT' : 'Asti',
			'AV' : 'Avellino',
			'BA' : 'Bari',
			'BT' : 'Barletta-Andria-Trani',
			'BL' : 'Belluno',
			'BN' : 'Benevento',
			'BG' : 'Bergamo',
			'BI' : 'Biella',
			'BO' : 'Bologna',
			'BS' : 'Brescia',
			'BR' : 'Brindisi',
			'CA' : 'Cagliari',
			'CL' : 'Caltanissetta',
			'CB' : 'Campobasso',
			'CE' : 'Caserta',
			'CT' : 'Catania',
			'CZ' : 'Catanzaro',
			'CH' : 'Chieti',
			'CO' : 'Como',
			'CS' : 'Cosenza',
			'CR' : 'Cremona',
			'KR' : 'Crotone',
			'CN' : 'Cuneo',
			'EN' : 'Enna',
			'FM' : 'Fermo',
			'FE' : 'Ferrara',
			'FI' : 'Florence',
			'FG' : 'Foggia',
			'FC' : 'Forlì-Cesena',
			'FR' : 'Frosinone',
			'GE' : 'Genoa',
			'GO' : 'Gorizia',
			'GR' : 'Grosseto',
			'IM' : 'Imperia',
			'IS' : 'Isernia',
			'SP' : 'La Spezia',
			'AQ' : 'L Aquila',
			'LT' : 'Latina',
			'LE' : 'Lecce',
			'LC' : 'Lecco',
			'LI' : 'Livorno',
			'LO' : 'Lodi',
			'LU' : 'Lucca',
			'MC' : 'Macerata',
			'MN' : 'Mantua',
			'MS' : 'Massa and Carrara',
			'MT' : 'Matera',
			'ME' : 'Messina',
			'MI' : 'Milan',
			'MO' : 'Modena',
			'MB' : 'Monza and Brianza',
			'NA' : 'Naples',
			'NO' : 'Novara',
			'NU' : 'Nuoro',
			'OR' : 'Oristano',
			'PD' : 'Padua',
			'PA' : 'Palermo',
			'PR' : 'Parma',
			'PV' : 'Pavia',
			'PG' : 'Perugia',
			'PU' : 'Pesaro and Urbino',
			'PE' : 'Pescara',
			'PC' : 'Piacenza',
			'PI' : 'Pisa',
			'PT' : 'Pistoia',
			'PN' : 'Pordenone',
			'PZ' : 'Potenza',
			'PO' : 'Prato',
			'RG' : 'Ragusa',
			'RA' : 'Ravenna',
			'RC' : 'Reggio Calabria',
			'RE' : 'Reggio Emilia',
			'RI' : 'Rieti',
			'RN' : 'Rimini',
			'RM' : 'Rome',
			'RO' : 'Rovigo',
			'SA' : 'Salerno',
			'SS' : 'Sassari',
			'SV' : 'Savona',
			'SI' : 'Siena',
			'SO' : 'Sondrio',
			'SU' : 'South Sardinia',
			'BZ' : 'South Tyrol',
			'SR' : 'Syracuse',
			'TA' : 'Taranto',
			'TE' : 'Teramo',
			'TR' : 'Terni',
			'TP' : 'Trapani',
			'TN' : 'Trento',
			'TV' : 'Treviso',
			'TS' : 'Trieste',
			'TO' : 'Turin',
			'UD' : 'Udine',
			'VA' : 'Varese',
			'VE' : 'Venice',
			'VB' : 'Verbano-Cusio-Ossola',
			'VC' : 'Vercelli',
			'VR' : 'Verona',
			'VV' : 'Vibo Valentia',
			'VI' : 'Vicenza',
			'VT' : 'Viterbo',
 		}
	},

	'FR' : {
		'name' : 'France',
		'states' : {
			'ARA' : 'Auvergne-Rhône-Alpes',
			'BFC' : 'Bourgogne-Franche-Comté',
			'BRE' : 'Brittany',
			'CVL' : 'Centre',
			'COR' : 'Corsica',
			'GES' : 'Grand Est',
			'HDF' : 'Hauts-de-France',
			'IDF' : 'Île-de-France',
			'NOR' : 'Normandy',
			'NAQ' : 'Nouvelle-Aquitaine',
			'OCC' : 'Occitanie',
			'PDL' : 'Pays de la Loire',
			'PAC' : 'Provence-Alpes-Côte dAzur',
 		}
	},	

	'Others' : {
		'name' : 'Others',
		'states' : {
			'Others' : 'Others'
		}
	}

}


# STRIPE SHIPPING SUPPORT 
stripe_shipping_support = {
	'US' : ['United States'],
	'CANADA' : ['Canada'],
	'UK' : ['United Kingdom'],
	'ASIA' : ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates' , 'Uzbekistan', 'Vietnam', 'Yemen'],
	'AUSTRALIA' : ['Australia'],
	'NEW ZEALAND': ['New Zealand'],
	'EUROPE' : ['Germany', 'France', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania', 'Netherlands', 'Belgium', 'Greece', 'Portugal', 'Sweden', 'Hungary', 'Belarus', 'Austria', 'Serbia', 'Switzerland', 'Bulgaria', 'Denmark', 'Finland', 'Slovakia', 'Norway', 'Ireland', 'Croatia', 'Moldova', 'Iceland', 'Monaco', 'Iceland'],
	'OTHER' : ['Other']
}

import datetime

now = datetime.datetime.now()
year = now.year + 6
years = list(range(1900, year))
years.reverse()


months = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}


