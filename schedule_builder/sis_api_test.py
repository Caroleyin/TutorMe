import requests

clist = [('MATH','3100'), ('PSYC','2150'), ('STAT','2120')]
url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1'
for c in clist:
    r = requests.get(url + '&subject=' + c[0] + '&catalog_nbr=' + c[1])
    for c in r.json():
        print(c['subject'], c['catalog_nbr'] + '-' + c['class_section'], c['component'], c['descr'], \
            c['class_nbr'], c['class_capacity'], c['enrollment_available'])