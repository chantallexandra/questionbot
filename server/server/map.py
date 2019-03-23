class Map:
    mapping_table = {'french': 'cuisine', 'japanese': 'cuisine', 'desserts': 'cuisine', 'seafood': 'cuisine',
                     'asian': 'cuisine', 'filipino': 'cuisine', 'indian': 'cuisine', 'sushi': 'cuisine',
                     'korean': 'cuisine', 'chinese': 'cuisine', 'european': 'cuisine', 'mexican': 'cuisine',
                     'american': 'cuisine', 'ice cream': 'cuisine', 'cafe': 'cuisine', 'italian': 'cuisine',
                     'pizza': 'cuisine', 'bakery': 'cuisine', 'mediterranean': 'cuisine', 'fast food': 'cuisine',
                     'brazilian': 'cuisine', 'arabian': 'cuisine', 'bar food': 'cuisine', 'grill': 'cuisine',
                     'international': 'cuisine', 'peruvian': 'cuisine', 'latin american': 'cuisine', 'burger': 'cuisine',
                     'juices': 'cuisine', 'healthy food': 'cuisine', 'beverages': 'cuisine', 'lebanese': 'cuisine',
                     'sandwich': 'cuisine', 'steak': 'cuisine', 'bbq': 'cuisine', 'gourmet fast food': 'cuisine',
                     'mineira': 'cuisine', 'north eastern': 'cuisine', '': 'cuisine', 'coffee and tea': 'cuisine',
                     'vegetarian': 'cuisine', 'tapas': 'cuisine', 'breakfast': 'cuisine', 'diner': 'cuisine',
                     'southern': 'cuisine', 'southwestern': 'cuisine', 'spanish': 'cuisine', 'argentine': 'cuisine',
                     'caribbean': 'cuisine', 'german': 'cuisine', 'vietnamese': 'cuisine', 'thai': 'cuisine',
                     'modern australian': 'cuisine', 'teriyaki': 'cuisine', 'cajun': 'cuisine', 'canadian': 'cuisine',
                     'tex-mex': 'cuisine', 'middle eastern': 'cuisine', 'greek': 'cuisine', 'bubble tea': 'cuisine',
                     'tea': 'cuisine', 'australian': 'cuisine', 'fusion': 'cuisine', 'cuban': 'cuisine',
                     'hawaiian': 'cuisine', 'salad': 'cuisine', 'irish': 'cuisine', 'new american': 'cuisine',
                     'soul food': 'cuisine', 'turkish': 'cuisine', 'pub food': 'cuisine', 'persian': 'cuisine',
                     'continental': 'cuisine', 'singaporean': 'cuisine', 'malay': 'cuisine', 'cantonese': 'cuisine',
                     'dim sum': 'cuisine', 'western': 'cuisine', 'finger food': 'cuisine', 'british': 'cuisine',
                     'deli': 'cuisine', 'indonesian': 'cuisine', 'north indian': 'cuisine', 'mughlai': 'cuisine',
                     'biryani': 'cuisine', 'south indian': 'cuisine', 'pakistani': 'cuisine', 'afghani': 'cuisine',
                     'hyderabadi': 'cuisine', 'rajasthani': 'cuisine', 'street food': 'cuisine', 'goan': 'cuisine',
                     'african': 'cuisine', 'portuguese': 'cuisine', 'gujarati': 'cuisine', 'armenian': 'cuisine',
                     'mithai': 'cuisine', 'maharashtrian': 'cuisine', 'modern indian': 'cuisine',
                     'charcoal grill': 'cuisine', 'malaysian': 'cuisine', 'burmese': 'cuisine', 'chettinad': 'cuisine',
                     'parsi': 'cuisine', 'tibetan': 'cuisine', 'raw meats': 'cuisine', 'kerala': 'cuisine',
                     'belgian': 'cuisine', 'kashmiri': 'cuisine', 'south american': 'cuisine', 'bengali': 'cuisine',
                     'iranian': 'cuisine', 'lucknowi': 'cuisine', 'awadhi': 'cuisine', 'nepalese': 'cuisine',
                     'drinks only': 'cuisine', 'oriya': 'cuisine', 'bihari': 'cuisine', 'assamese': 'cuisine',
                     'andhra': 'cuisine', 'mangalorean': 'cuisine', 'malwani': 'cuisine', 'cuisine varies': 'cuisine',
                     'moroccan': 'cuisine', 'naga': 'cuisine', 'sri lankan': 'cuisine', 'peranakan': 'cuisine',
                     'sunda': 'cuisine', 'ramen': 'cuisine', 'kiwi': 'cuisine', 'asian fusion': 'cuisine',
                     'taiwanese': 'cuisine', 'fish and chips': 'cuisine', 'contemporary': 'cuisine', 'scottish': 'cuisine',
                     'curry': 'cuisine', 'patisserie': 'cuisine', 'south african': 'cuisine', 'durban': 'cuisine',
                     'kebab': 'cuisine', 'turkish pizza': 'cuisine', 'izgara': 'cuisine', 'world cuisine': 'cuisine',
                     'd√å_ner': 'cuisine', 'restaurant cafe': 'cuisine', 'b√å_rek': 'cuisine', 'makati city': 'city',
                     'mandaluyong city': 'city', 'pasay city': 'city', 'pasig city': 'city', 'quezon city': 'city',
                     'san juan city': 'city', 'santa rosa': 'city', 'tagaytay city': 'city', 'taguig city': 'city',
                     'brasì_lia': 'city', 'rio de janeiro': 'city', 'sì£o paulo': 'city', 'albany': 'city',
                     'armidale': 'city', 'athens': 'city', 'augusta': 'city', 'balingup': 'city', 'beechworth': 'city',
                     'boise': 'city', 'cedar rapids/iowa city': 'city', 'chatham-kent': 'city', 'clatskanie': 'city',
                     'cochrane': 'city', 'columbus': 'city', 'consort': 'city', 'dalton': 'city', 'davenport': 'city',
                     'des moines': 'city', 'dicky beach': 'city', 'dubuque': 'city', 'east ballina': 'city',
                     'fernley': 'city', 'flaxton': 'city', 'forrest': 'city', 'gainesville': 'city',
                     'hepburn springs': 'city', 'huskisson': 'city', 'inverloch': 'city', 'lakes entrance': 'city',
                     'lakeview': 'city', 'lincoln': 'city', 'lorn': 'city', 'macedon': 'city', 'macon': 'city',
                     'mayfield': 'city', 'mc millan': 'city', 'middleton beach': 'city', 'miller': 'city', 'monroe': 'city',
                     'montville': 'city', 'ojo caliente': 'city', 'orlando': 'city', 'palm cove': 'city', 'paynesville': 'city',
                     'penola': 'city', 'pensacola': 'city', 'phillip island': 'city', 'pocatello': 'city', 'potrero': 'city',
                     'princeton': 'city', 'rest of hawaii': 'city', 'savannah': 'city', 'singapore': 'country_name',
                     'sioux city': 'city', 'tampa bay': 'city', 'tanunda': 'city', 'trentham east': 'city', 'valdosta': 'city',
                     'vernonia': 'city', 'victor harbor': 'city', 'vineland station': 'city', 'waterloo': 'city',
                     'weirton': 'city', 'winchester bay': 'city', 'yorkton': 'city', 'abu dhabi': 'city', 'dubai': 'city',
                     'sharjah': 'city', 'agra': 'city', 'ahmedabad': 'city', 'allahabad': 'city', 'amritsar': 'city',
                     'aurangabad': 'city', 'bangalore': 'city', 'bhopal': 'city', 'bhubaneshwar': 'city',
                     'chandigarh': 'city', 'chennai': 'city', 'coimbatore': 'city', 'dehradun': 'city',
                     'faridabad': 'city', 'ghaziabad': 'city', 'goa': 'city', 'gurgaon': 'city', 'guwahati': 'city',
                     'hyderabad': 'city', 'indore': 'city', 'jaipur': 'city', 'kanpur': 'city', 'kochi': 'city',
                     'kolkata': 'city', 'lucknow': 'city', 'ludhiana': 'city', 'mangalore': 'city', 'mohali': 'city',
                     'mumbai': 'city', 'mysore': 'city', 'nagpur': 'city', 'nashik': 'city', 'new delhi': 'city',
                     'noida': 'city', 'panchkula': 'city', 'patna': 'city', 'puducherry': 'city', 'pune': 'city',
                     'ranchi': 'city', 'secunderabad': 'city', 'surat': 'city', 'vadodara': 'city', 'varanasi': 'city',
                     'vizag': 'city', 'bandung': 'city', 'bogor': 'city', 'jakarta': 'city', 'tangerang': 'city',
                     'auckland': 'city', 'wellington city': 'city', 'birmingham': 'city', 'edinburgh': 'city',
                     'london': 'city', 'manchester': 'city', 'doha': 'city', 'cape town': 'city', 'inner city': 'city',
                     'johannesburg': 'city', 'pretoria': 'city', 'randburg': 'city', 'sandton': 'city', 'colombo': 'city',
                     'ankara': 'city', '€¡stanbul': 'city', 'india': 'country_name', 'australia': 'country_name', 'brazil': 'country_name',
                     'canada': 'country_name', 'indonesia': 'country_name', 'new zealand': 'country_name', 'phillipines': 'country_name',
                     'qatar': 'country_name', 'south africa': 'country_name', 'sri lanka': 'country_name', 'turkey': 'country_name',
                     'uae': 'country_name', 'united kingdom': 'country_name', 'united states': 'country_name', 'excellent': 'rating_text',
                     'very good': 'rating_text', 'good': 'rating_text', 'average': 'rating_text', 'not rated': 'rating_text',
                     'poor': 'rating_text', 'botswana pula(p)': 'currency', 'brazilian real(r$)': 'currency',
                     'dollar($)': 'currency', 'emirati diram(aed)': 'currency', 'indian rupees(rs.)': 'currency',
                     'indonesian rupiah(idr)': 'currency', 'newzealand($)': 'currency', 'pounds(å£)': 'currency',
                     'qatari rial(qr)': 'currency', 'rand(r)': 'currency', 'sri lankan rupee(lkr)': 'currency',
                     'turkish lira(tl)': 'currency'}
