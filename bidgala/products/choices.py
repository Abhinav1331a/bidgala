color = {
	'#000' : {
		'group' : ['#000', '#444', '#666', '#999', '#ccc'],
		'id' : 'color-1',
		'name' : 'Black'
	},

	'#fff' : {
		'group' : ['#eee', '#f3f3f3', '#fff'],
		'id' : 'color-2',
		'name' : 'White'
	},

	'#f00' : {
		'group' : ['#f00', '#f4cccc', '#ea9999', '#e06666', '#c00', '#900', '#600'],
		'id' : 'color-3',
		'name' : 'Red'
	},

	'#f90' : {
		'group' : ['#f90', '#fce5cd', '#f9cb9c', '#f6b26b', '#e69138', '#b45f06', '#783f04'],
		'id' : 'color-4',
		'name' : 'Orange'
	},

	'#f1c232' : {
		'group' : ['#f1c232', '#ff0', '#fff2cc', '#ffe599', '#ffd966', '#bf9000', '#7f9000'],
		'id' : 'color-5',
		'name' : 'Yellow'
	},

	'#6aa84f' : {
		'group': ['#6aa84f', '#00ff00', '#d9ead3', '#b6d7a8', '#93c47d', '#38761d', '#274e13'],
		'id' : 'color-6',
		'name' : 'Green'
	},

	'#a2c4c9' : {
		'group' : ['#a2c4c9', '#00ffff', '#74a5af', '#45818e', '#134f5c', '#0c343d'],
		'id' : 'color-7',
		'name' : 'Mint'
	},

	'#00f' : {
		'group' : ['#00f', '#cfe2f3', '#9fc5e8', '#6fa8dc', '#3d85c6', '#0b5394', '#073763'],
		'id' : 'color-8',
		'name' : 'Blue'
	},

	'#674ea7' : {
		'group' : ['#674ea7', '#351c75', '#20124d', '#8e7cc3', '#b4a7d6', '#d9d2e9', '#90f'],
		'id' : 'color-9',
		'name' : 'Purple'
	},

	'#a64d79' : {
		'group' : ['#a64d79', '#741b47', '#4c1130', '#c27ba0', '#d5a6bd', '#ead1dc', '#f0f'],
		'id' : 'color-10',
		'name' : 'Pink'
	}
}


dim_measurement = {
	'Meter' : 'm',
	'Centimeter' : 'cm',
	'Inches' : 'inches'
}
 

styles = {
	'abstract':'Abstract',
	'contemporary':'Contemporary',
	'figurative':'Figurative',
	'minimalist':'Minimalist',
	'portraiture':'Portraiture',
	'landscape':'Landscape',
	'fashion':'Fashion',
	'popart':'Pop Art',
	'other' : 'Other'
}


material = {
	'canvas' : 'Canvas',
	'paper' : 'Paper',
	'wood' : 'Wood',
	'cardboard' : 'Cardboard',
	'soft' : 'Soft (Yam, Cotton, Fabric)',
	'plastic' : 'Plastic',
	'aluminum' : 'Aluminum',
	'glass' : 'Glass',
	'carbonfibre': 'Carbon Fibre',
	'steel' : 'Steel',
	'iron' : 'Iron',
	'bronze' : 'Bronze',
	'ceramic' : 'Ceramic',
	'stone' : 'Stone',
	'stainlesssteel' : 'Stainless Steel',
	'marble' : 'Marble',
	'other' : 'Other',

}

sub_type_one = {
	'abstract' : 'Abstract',
	'animalsBirdsFish' : 'Animals, Birds & Fish',
	'astronomySpace' : 'Astronomy & Space',
	'buildingsArchitecture' : 'Buildings & Architecture',
	'childrensArt' : "Children's Art",
	'entertainment' : 'Entertainment',
	'ethnicCulturalTribal' : 'Ethnic, Cultural & Tribal',
	'fantasyMythology' : 'Fantasy & Mythology',
	'flowersPlantsTrees' : 'Flowers, Plants & Trees',
	'foodBeverage' : 'Food & Beverage',
	'holidaysOccasions' : 'Holidays & Occasions',
	'humorSatire' : 'Humor & Satire',
	'landscapesNature' : 'Landscapes & Nature',
	'peopleFigures' : 'People & Figures',
	'placesTravel' : 'Places & Travel',
	'politicsPatriotism' : 'Politics & Patriotism',
	'religionPhilosophyAstrology' : 'Religion, Philosophy & Astrology',
	'scienceTechnology' : 'Science & Technology',
	'sportsHobbies' : 'Sports & Hobbies',
	'stillLife': 'Still Life',
	'vehiclesTransportation' : 'Vehicles & Transportation'
}



sub_type_two = {

	'bowlsPots': 'Bowls & Pots',
	'candleHolders': 'Candle Holders',
	'childrensArt': "Children's Art",
	'cupsGoblets': 'Cups Goblets',
	'figurative': 'Figurative',
	'fountainsWaterwalls': 'Fountains & Waterwalls',
	'jars': 'Jars',
	'jewelry': 'Jewelry',
	'masks': 'Masks',
	'mugsTankards': 'Mugs & Tankards',
	'ornaments': 'Ornaments',
	'pitchersJugs': 'Pitchers & Jugs',
	'platesSaucers': 'Plates & Saucers',
	'plattersTrays': 'Platters & Trays',
	'saltPepperShakers': 'Salt & Pepper Shakers',
	'sculpturalArtistic': 'Sculptural & Artistic',
	'teapotsSets': 'Teapots & Sets',
	'tiles': 'Tiles',
	'vasesUrns': 'Vases & Urns',
	'otherCeramics': 'Other Ceramics'

}


grouped_sub_type = {
	**sub_type_one, **{'other' : 'Other'}
}

category = {
	'paintings' : 'Paintings',
	'prints' : 'Prints',
	'drawingIllustration' : 'Drawing & Illustration',
	'photography' : 'Photography',
	'sculptures' : 'Sculptures',
	'mixedMedia' : 'Mixed Media'

}

category_sell = {
	'paintings' : 'Paintings',
	'prints' : 'Prints',
	'drawingIllustration' : 'Drawing & Illustration',
	'photography' : 'Photography',
	'sculptures' : 'Sculptures',
	'ceramicPottery' : 'Ceramic & Pottery',
	'glass' : 'Glass',


}


subcategory = {

	'glass' : sub_type_two,
	'sculptures' : sub_type_one,
	'ceramicPottery' : sub_type_two,
	'photography' : sub_type_one,
	'drawingIllustration' : sub_type_one,
	'paintings' : sub_type_one,
	'prints' : sub_type_one
}
