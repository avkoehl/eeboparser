# prepositions, pronouns, authors, variations of printed
# various stopwords, months, locations such as alley, 
# n and ne are for new england
# note that there are - within words
# also some accents
locations_blacklist = [
"enprynted",
"imprynted",
"imprented",
"anno",
"are",
"for",
"of",
"within",
"by",
"at",
"domini",
"printio",
"the",
"and",
"in",
"sic",
"re",
"im",
"jm",
"er",
"em",
"an",
"yn",
"en"
"a",
"ad",
"briniwyd",
"brintio",
"brio",
"prynted",
"imprinted",
"printed",
"baker",
"xi",
"octoberdo",
"robert",
"ymlen",
"last",
"february",
"daye",
"west",
"smithfield",
"cliefe ",
"lande",
"we",
"know",
"where",
"whan",
"judge",
"you",
"place",
"can",
"to",
"theater",
"translated",
"thackwell",
"south",
"stampato",
"gait",
"southern",
"on",
"back-side",
"cyclopean",
"mountains",
"sold",
"p",
"sheet",
"september",
"blew",
"bitche",
"doglane",
"ratisbonne",
"pruntiedig",
"ptinted",
"published",
"prointed",
"printiedic",
"print",
"preintiedig",
"prented",
"prentid",
"prentit",
"pranted",
"place",
"not",
"farre",
"cum",
"privilegio",
"octob",
"newely",
"newlie",
"m",
"may",
"mdxlix",
"made",
"stephen",
"buckley",
"smithfield",
"parsih",
"saynt",
"barthelmewes",
"hospitall",
"special",
"order",
"temstrete",
"ouer",
"agaynste",
"stiliardes",
"dobbel",
"hood",
"three",
"cranes",
"vintree",
"to",
"prevent",
"mis-information",
"stephen",
"buckley",
"re-painted",
"paules",
"churche",
"yarde",
"sygne",
"holye",
"ghost",
"churcheyarde",
"signe",
"lucrece",
"holy",
"ghost",
"poules",
"povvles",
"powles",
"temple",
"barre",
"hande",
"starre",
"hand",
"fleetestreate",
"beneath",
"conduit",
"signe",
"john",
"euangelist",
"fleetestete",
"flete",
"strete",
"sonne",
"nere",
"vnto",
"sayncte",
"dunstons",
"aldergate",
"strete",
"blacke",
"friers",
"not",
"profit",
"but",
"common",
"weles",
"good",
"no",
"where",
"to",
"be",
"sold",
"but",
"some",
"where",
"to",
"be",
"given",
"iohn",
"wright",
"mathew",
"collins",
"three",
"black",
"birds",
"cannon-street",
"robert",
"barker",
"assignes",
"john",
"bill",
"william",
"grantham",
"cock-pit",
"alley",
"near",
"ih",
"t",
"ryder",
"licensed",
"according",
"order",
"drury-lane",
"really",
"abroad",
"jmprented",
"jmprentit",
"july",
"fetestrete",
"sygne",
"rose",
"garlande",
"robert",
"copland",
"imprynded",
"imprnted",
"impryntid",
"impynted ",
"inpryntyd ",
"iohn",
"legat",
"&",
"aux",
"impressum",
"impressus",
"impressa",
"impresso",
"imprime",
"imprimée",
"nouuellement",
"imprined",
"imprinnted",
"imprínted ",
"imprînted",
"imprentit",
"â ",
"imprined",
"à ",
" ̀",
"xx",
"day",
"mowneth",
"may",
"impress",
"imprentyt",
"imprentyd",
"impreneted",
"impkinted",
"at",
"ig",
"ianuarij",
"primus",
"his",
"majesties",
"command",
"decemb",
"ianuary",
"haue",
"march",
"gedruckt",
"haec",
"naer",
"van",
"'s",
"gravenhage",
"tot",
"fynyshhed",
"thabbey",
"our",
"heart",
"excussum",
"excudebat",
"from",
"first",
"towne",
"enprentyd",
"enprented",
"exempt",
"monastery",
"tauestok",
"ye",
"famous",
"cite",
"emprentyd ",
"emprented",
"ye",
"day",
"july",
"re-",
"conform",
"to",
"copy",
"christopher",
"higgins",
"harts-close",
"over",
"against",
"trone-church",
"decemb",
"darby-house",
"cyte",
"with",
"licence",
"brintiwyd",
"brintwyd",
"brintywyd",
"ir",
"awdwr",
"ar",
"na",
"chur",
"ngclò ",
"ndùn-éduin",
"att",
"i",
"brintio",
"printio",
"a\'i",
"ad",
"ai",
"brio",
"printfodd",
"printio",
"ag",
"briniwyd",
"amongst",
"city",
"marchandise",
"knowen",
"vnto",
"india",
"all",
"limites",
"earth",
"naar",
"de",
"copie",
"gedruckt",
"md",
"argraphedig",
"argraphwyd",
"argraphwŷd",
"then",
"nowe",
"duflan",
"y",
"yng",
"att",
"atte",
"audomari",
"dem",
"zu",
"und",
"rach",
"aussgegertigt", 
"gedruckten",
"exemplar",
"be",
"newly",
"betweene",
"skye",
"grounde",
"vvithin",
"myle",
"oake",
"not",
"many",
"fieldes",
"n ",
"e ",
"ne ",
"breintiuyd",
"breintivvyd",
"ninas",
"nov",
"ang",
"anglorum",
"do",
"so",
"diuireadh",
"ngclò",
"ndùn-edin"
]
# individual word variations
# based on a non-experts reading of unique locations
# in the locations column sorted alphabetically
# variations are due to spelling, language and transcription errors
single_word_variations = {
#
# BASEL (Basel, Switzerland)
"basil": "basel",
"basill": "basel",
"basyl": "basel",
#
# DOWAY (Douai, France)
"douay": "doway",
"douai": "doway",
"douay": "doway", 
"doüay": "doway", 
"dovvay": "doway",
"dovvay": "doway", 
"dowa": "doway",
"dowaie": "doway",
#
# DENSHIRE (unknown)
"denshyre": "denshire",
#
# DUBLIN (Dublin, Ireland)
"dubdin": "dublin",
"dubline": "dublin",
"dublinii": "dublin",
"dvblin": "dublin",
#
# FRANKFURT (Frankfurt, Germany)
"franckford": "frankfurt",
"franckfort": "frankfurt",
"francofourd": "frankfrut",
#
# EDINBURGH (Edinburgh, Scotland)
"eclinburgh": "edinburgh",
"edenborough": "edinburgh",
"edenbrough": "edinburgh",
"edenburg": "edinburgh",
"edenburgh": "edinburgh",
"edenburgi": "edinburgh",
"ediburgh": "edinburgh",
"edimbourg": "edinburgh",
"edinb": "edinburgh",
"edinbourg": "edinburgh",
"edinbrugh": "edinburgh",
"edinburg":  "edinburgh",
"edinburghi": "edinburgh",
"edinburgi": "edinburgh",
"edinburh": "edinburgh",
"edinbvrgh": "edinburgh",
"edingborough": "edinburgh",
"edingburgh": "edinburgh",
"edinnburgi": "edinburgh",
"edynburgh": "edinburgh",
#
# MARLBOROUGH (Marlborough, England)
"malborow": "marlborough",
"marborow": "marlborough",
"marlborow": "marlborough",
#
# DELFT (Delf, Netherlands)
"delf": "delft",
"delff": "delft",
"delph": "delft",
#
# CANTERBURY (Canterbury, England)
"cantabrigiae": "canterbury",
"cantabrigiæ": "canterbury",
"cantebrig": "canterbury",
"cantorbury": "canterbury", 
"cantebrigiæ": "canterbury",
"canterbury": "canterbury",
"cantorbury": "canterbury",
#
# COLLEN (unknown)
"colloniæ": "collen",
#
# CORK (Cork, Ireland)
"corck": "cork",
"corcke": "cork",
"cork": "cork",
#
# MALMO (Malmo, Sweden)
"malmoo": "malmo",
"malmö": "malmo",
#
# PARIS (Paris, France)
"parisiis": "paris",
"parisius": "paris",
"parise": "paris",
"parys": "paris",
#
# WESTMINSTER (Westminster, England)
"westmystre": "westminster",
"westmonstre": "westminster",
"westmynster": "westminster",
"westmynstre": "westminster",
"westmyster": "westminster",
"westmonasterii": "westminster",
"westmestre": "westminster",
"westmynstre": "westminster",
"westmoster": "westminster",
"westemynster": "westminster",
"westmester": "westminster",
"westmestre": "westminster",
"westminister": "westminster",
#
# WITTENBERG (Wittenberg, Germany)
"wittenberge": "witteberg",
#
# HEMEL HEMPSTEAD (Hemel Hempstead, England)
"hemstead": "hemel hempstead",
#
# HEIDELBERG (Heidelberg, Germany)
"heidelbergh": "heidelberg",
#
# HAMBURG (Hamburg, Germany)
"hamborough": "hamburg",
"hamboroughe": "hambrug",
"hamburgh": "hambrug",
#
# DURHAM (Durham, England)
# gatesehead maps to durham because of appearance of gateside ie gateshead durham
"gateshead": "durham",
"gateside": "durham",
#
# GHENT (Ghent, Belgium)
"gente": "ghent",
"gant": "ghent",
#
# MWYTHIG (unknown)
"mwŷthig": "mwythig",
#
# BRISTOL (Bristol, England)
"bristoll": "bristol",
#
# BRUSSELS (Brussels, Belgium)
"bruxelles": "brussels",
"bruxells": "brussels",
#
# GLASGOW (Glasgow, Scotland)
"glasgovv": "glasgow",
"glasguæ": "glasgow",
#
# GENEVA (Geneva, Switzerland)
"geneua": "geneva",
"genevah": "geneva",
#
# CAMBRDIGE (Cambridge, England)
# for US cambridge check two_word_variations
"cambridg": "cambridge",
#
# GREENWICH (Greenwich, England)
"grenewych": "greenwich",
#
# VENICE (Venice, Italy)
"venetia": "venice",
"ventiis": "venice",
"venus": "venice",
"venez": "venice",
#
# TOULOUSE (Toulouse, France)
"tolose": "toulouse",
#
# NETHERLANDS (Netherlands)
"lowcountryes": "netherlands",
#
# LOUVAIN (Leuven, Belgium)
"louain": "louvain",
"louaine": "louvain",
"louan": "louvain",
"louanii": "louvain",
"louayne": "louvain",
"lovain": "louvain",
"lovanii": "louvain",
"lovanni": "louvain",
#
# OXFORD (Oxford, England)
"oxoniæ": "oxford",
"oxonii": "oxford",
"oxen": "oxford",
"oxforde": "oxford",
"oxenford": "oxford",
#
# SOUTHWARK (Southwark, London, England)
"southwarke":"southwark",
"sowthwarke":"southwark",
"sothewarke":"southwark",
#
# LONDON (London, England)
"londra": "london",
"oonden": "london",
"nod-nol": "london",
"lunnduin": "london",
"lundain": "london",
"lundon": "london",
"loydon": "london",
"loudon": "london",
"londonn": "london",
"londoon": "london",
"londonian": "london",
"londou": "london",
"londra": "london",
"londre": "london",
"londrun": "london",
"lonini": "london",
"lonkon": "london",
"lonlon": "london",
"lonndini": "london",
"lonndo": "london",
"lonndon": "london",
"lonnon": "london",
"lonodnsic": "london",
"lonon": "london",
"londnon": "london",
"londom": "london",
"lo": "london",
"loddon": "london",
"lodnon": "london",
"lodon": "london",
"lond": "london",
"londen": "london",
"londgn": "london",
"londin": "london",
"londrez": "london",
"londonijs": "london",
"londres": "london",
"lond": "london",
"llùndain": "london",
"londdn": "london",
"londinesis": "london",
"llundain": "london",
"londini": "london",
"lbndon": "london",
#
# HAARLEM (Haarlem, Netherlands)
"haarlem": "haarlem",
#
# HAGUE (The Hague, Netherlands)
"hagæ": "the hague",
"hage": "the hague",
"hagh": "the hague",
"haghe": "the hague",
#
# AMSTERDAM (Amsterdam, Netherlands)
"amstelrodam": "amsterdam",
"ampsterdam": "amsterdam",
"amstelodami": "amsterdam",
"amselredam": "amsterdam",
"amstelredam": "amsterdam",
"amsterledam": "amsterdam",
"amsterodam": "amsterdam",
"amstredam": "amsterdam",
"antwerpen": "amsterdam",
#
# EUROPE (unknown)
"europ": "europe",
#
# ANTWERP (Antwerp, Netherlands)
"andwarpe": "antwerp",
"andewerpe": "antwerp",
"andwerpe": "antwerp",
"antuarpe": "antwerp",
"antuerpiae": "antwerp",
"antuerpiæ": "antwerp",
"antverpiae": "antwerp",
"antberpiæ": "antwerp",
"antvverp": "antwerp",
"antvverpe": "antwerp",
"antwarp": "antwerp",
"antwerp": "antwerp",
"antwerpe": "antwerp",
"antwerpen": "antwerp",
"antwerpiæ": "antwerp",
"antwrop": "antwerp",
"anvverpe": "antwerp",
"anwerp": "antwerp",
"anwerpe": "antwerp",
#
# IPSWICH (Ipswich, England)
"ippeswich": "ipswich",
"ippeswych": "ipswich",
"ippiswich": "ipswich",
"ippiswiche": "ipswich",
"ippyswiche": "ipswich",
"ippyswyche": "ipswich",
#
# LEIDEN (Leiden, Netherlands)
"leyden": "leiden",
#
# LIEGE (Liege, Belgium)
"liège": "liege",
#
# WITTENBERG (Wittenberg, Germany)
"wittonburge": "wittenberg",
"wyttonburge": "wittenberg",
#
# BLACKFRIARS (Blackfriars, England)
"blackefriers": "blackfriars",
#
# ROTTERDAM (Rotterdam, Netherlands)
"roterdame": "rotterdam",
#
# ABERDEEN (Aberdeen, Scotland)
"aberden": "aberdeen",
"aberdene": "aberdeen",
"aberdoniæ": "aberdeen",
"aberdoniis": "aberdeen",
"abredeis": "aberdeen",
#
# MIDDLESBROUGH (Middlesbrough, England)
"middelborg": "middlesbrough",
"middelborough":  "middlesbrough",
"middelburg":  "middlesbrough",
"middelburgh":  "middlesbrough",
"middleborrowgh":  "middlesbrough",
"middleborrow":  "middlesbrough",
"middleborugh":  "middlesbrough",
"middlebourgh":  "middlesbrough",
"middleburgh":  "middlesbrough",
"middlebrugh":  "middlesbrough",
"midleburgh":  "middlesbrough",
#
# ROUEN (Rouen, France)
"roan": "rouen",
"rouan": "rouen",
"roüen": "rouen",
"rowen": "rouen",
#
# RHEIMS (Reims, France)
"rheins": "rheims",
"rhemes": "rheims",
# 
# SAINT-ANDREWS (Saint Andrews, Scotland)
"sanctandrois": "saint-andrews",
#
# SAVOY (Savoie, France)
"saouy": "savoy",
"savoye": "savoy",
#
# STRASBOURG (Strasbourg, France)
"strasborowe": "strasbourg",
"straszburg": "strasbourg",
#
# STRIVELING (Unknown)
"striuling": "striveling",
#
# YORK (York, England)
"yorke": "york",
#
# WORCESTER (Worcester, England)
"worceter": "worcester",
#
# ZURICH (Zurich, Switzerland)
"zijrik": "zurich",
"zurych": "zurich",
"zürich": "zurich",
"ziiryk": "zurich",
"zurik": "zurich",
#
# WATERFORD (Waterford, England)
"vvaterford": "waterford",
"warerford": "waterford",
#
# WESEL (Wesel, Germany)
"wesill": "wesel",
#
# UTRECTH (Utrecht, Netherlands)
"vtrech": "utrecht",
"vtrecth": "utrecht",
"vtricht": "utrecht",
}
# multi word variations
# based on non-experts reading of unique locaitons
# in the locations column sorted alphabetically
# variations due to spelling, language and transcription erros
# often times the second word is a region or country name
# add ie's where necessary
# note its planned to use this after the single word mappings

phrase_variations = {
#
# EXETER (Exeter, England)
"exeter devon": "exeter",
#
# DOUAI (Douai, France)
"douay douai": "douai",   
"dovvay rheims": "douai",
"dowa ie douai": "douai",
#
# DUBLIN (Dublin, Ireland)
"dublin edinburgh": "dublin ie edinburgh",
"dublin london": "dublin ie london",
#
# FRANKFURT (Frankfurt, Germany) 
"francoforti moenum": "frankfurt",
#
# EDINBURGH (Edinburgh, Scotland)
"holy-rood-house edinburgh": "edinburgh",
"holy-rood-house ie edinburgh": "edinburgh",
"edinburgh or st andrews": "edinburg",
"edenborough scotland": "edinburgh",
"edenburgh london": "edinburgh ie london",
"edinburg london": "edinburgh ie london",
"edinburgh london": "edinburgh ie london",
"edinburgh aberdene": "edinburgh ie aberdene",
"edinburgh glasgow": "edinburgh ie glasgow",
"edinbvrgh london": "edinburgh ie london",
#
# ELEUTHEROPOLIS (unknown)
"eleutheropolis oxford": "eleutheropolis ie oxford",
#
# DELFT (Delft, Netherlands)
"delf holeand": "delft",
"delph holland": "delft",
#
# BOSTON (Boston, United States)
"massachuset boston": "boston",
"boston mass": "boston",
"boston massachusets": "boston",
"boston massachusetts": "boston",
"boston new england": "boston",
"boston new-england": "boston",
"boston new=england": "boston",
#
# PHILADELPHIA (Philadelphia, United States)
"philadelphia pennsylvania": "philadelphia",
#
# SAINT-OMER (Saint-Omer, France)
"st omers": "saint-omer",
"st-omer": "saint-omer",
"st omer": "saint-omer",
"s omers": "saint-omer",
"s omers ie saint omers": "saint-omer",
"saint-omer france": "saint-omer",
#
# WESTMINSTER (Westminster, England)
"westminster (london)": "westminster",
"westminster london": "westminster",
#
# HEMEL HEMPSTEAD (Hemel Hempstead, Netherlands)
"ie hemel hempstead": "hemel hempstead",
#
# DURHAM (Durham, England)
"gateside ie gateshead durham": "durham",
#
# GHENT (Ghent, Netherlands)
"gant holland": "ghent",
"gant ie ghent": "ghent",
"gant ghent": "ghent",
#
# BRISTOL (Bristol, England)
"bristoll avon": "bristol",
#
# GLASGOW (Glasgow, Scotland)
"glasgow scotland": "glasgow",
#
# CAMBRDIGE (Cambridge, England)
"cambridge england": "cambridge",
"cambridge cambridgeshire": "cambridge",
"cambridge london": "cambridge",
#
# CAMBRDIGE MASSACHUSSETTS (Cambridge, United States)
"cabridg mass": "cambridge massachussetss",
"cabridge mass": "cambridge massachussetts",
"cambridge new-england": "cambridge massachussetts",
#
# VEVAY (Vevay, Switzerland)
"vevay switzerland": "vevay",
#
# NETHERLANDS (Netherlands)
"low countries": "netherlands",
#
# NORWICH (Norwich, England)
"norwich england": "norwich",
#
# OXFORD (Oxford, England)
"oxford eng": "oxford",
"oxon oxford": "oxford",
"oxford oxfordshire": "oxford",
"oxford i e london": "oxford ie london",
"oxford ielondon": "oxford ie london",
"oxford london":  "oxford ie london",
"oxford or london": "oxford ie london",
"oxfordie london": "oxford ie london",
# 
# LONDON (London, England)
"london london": "london",
"yondon ie london": "london",
"vtopia ie london": "london",
"sondon ie london": "london",
"lond ie london": "london", 
"england london": "london",
"colledge savoy london": "london",
"london ie london": "london",
"lonain ie london": "london",
"london southwarke": "london",
"londoa ie london": "london",
"nod-lon ie london": "london",
"obedience ie london": "london",
"ondon ie london": "london",
"ie london": "london",
"london little britaine": "london",
"london or middelburgh": "london",
"london ouer aldersgate": "london",
"london church": "london",
"london entred": "london",
"london etc": "london",
"london sn": "london",
"london al": "london",
"t london": "london",
"nod-nol ie london": "london",
"londons ie london": "london",
"london york london": "london",
"london york stephen buckley london": "london",
"loneon ie london": "london",
"lonon ie london": "london",
"lonnon ie london": "london",
"london oxford":  "london ie oxford",
"london glasgow": "london ie glasgow",
"london edinburgh":  "london ie edinburgh",
"london savoy": "london ie savoy",
"london savoye": "london ie savoy",
"london la savoye":"london ie savoy",
"london leith": "london ie leith",
#
# LEITH (Leith, Ediburgh, Scotland)
"leith leith leith london leith leith scotland": "leith",
# 
# LEIDEN (Leiden, Netherlands)
"leiden holland": "leiden",
#
# THE HAGUE (The Hague, Netherlands)
"gravenhagh": "the hague",
"graven-hage": "the hague",
"s'grauen-haghe": "the hague",
"s'graven haghe": "the hague",
"sgrauen-haghe": "the hague",
"sgraven-haghe": "the hague",
"ad haghe hague": "the hague",
"la haye": "the hague",
"hagæ-comitis ie hague": "the hague",
"haghe ie hague": "the hague",
"gravenhagh netherlands": "the hague",
"hague london": "hague ie london",
#
# ANTWERP (Antwerp, Netherlands)
"n ie antwerp": "antwerp",
"duchye braband andewarpe": "antwerp",
#
# LEIDEN (Leiden, Netherlands)
"leyden london" : "leiden ie london",
"leiden london" : "leiden ie london",
#
# ROTTERDAM (Rotterdamn, Netherlands)   
"rotterdame holland": "rotterdam",
#
# ROCHESTER (Rochester, England)
"rochester kent england": "rochester",
#
# ABERDEEN (Aberdeen, Scotland)
"aberdeen scotland": "aberdeen",
#
# sl
"s l": "sl",
#
# SAINT-ALBANS (St Albans, England)
"st albans": "saint-albans",
"sanctus albanus": "saint-albans",
#
# SAINT-ANDREWS (Saint Andrews, Scotland)
"st andrews": "saint-andrews",
"sanct androus": "saint-andrews",
"sainct-andrevves": "saint-andrews",
"sainct-andrewes": "saint-andrews",
"sainct-andrews": "saint-andrews",
#
# SAINT-GERMAIN (Unknown)
"st germain": "saint-germain",
"st germains": "saint-germain",
"st germans": "saint-germain",
#
# SHOREDITCH (Shoreditch, England)
"shoreditch england": "shoreditch",
#
# STRASBOURG (Strasbourg, France)
"strasburgh elsas": "strasbourg",
# 
# STRIVELING (Unknown)
"striveling scotlande": "striveling",
#
# SWARTHMORE (Swarthmore, England)
"swarthmore england": "swarthmore",
#
# YORK (York, England)
"york engalnd": "york",
"york england": "york",
"yrok engalnd": "york",
"yrok england": "york",
"york now london": "york",
"yorke yorkshire": "york",
"york yorkshire": "york",
"york london": "york ie london",
"yorke london": "york ie london",
"yorke oxford": "york ie oxford",
"york oxford": "york ie oxford",
#
# WORCESTER (Worcester, England)
"worcesterim dorceter": "worcester",
"worcester worcestershire": "worcester",
#
# WATERFORD (Waterford, England)
"vvaterford waterford": "waterford",
"waterford ireland": "waterford",
"waterford waterford": "waterford",
#
# MILAN (Milan, Italy)
"ie milan": "milan"
}
