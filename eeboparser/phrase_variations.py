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
