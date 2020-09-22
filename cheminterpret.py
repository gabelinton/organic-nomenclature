
# INPUTS

while (True):

    hydrocarbon = ''
    branch = ''
    fhalo = ''
    clhalo = ''
    bhalo = ''
    ihalo = ''
    hydroxy = ''
    carhydrocarbon = ''
    valid = True
    cmol = 0
    hmol = 0
    bcmol = 0
    bhmol = 0
    fmol = 0
    clmol = 0
    bmol = 0
    imol = 0
    brantotal = 0
    alcmol = 0
    acidmol = 0
    carbox = False

    cmol = int(input('\nEnter total number of carbons: '))
    hmol = int(input('Enter total number of hydrogens and halogens: '))

    askforbran = input('Are any of those molecules branched? (-yl groups only): ')

    if (askforbran == 'Yes' or askforbran == 'yes'):

        brantotal = int(input('How many branched molecule groups are there?: '))
        bcmol = int(input('Enter number of branched carbons: '))
        bhmol = int(input('Enter number of branched hydrogens: '))
        
    askforhalo = input('Are there any halogens?: ')

    if (askforhalo == 'Yes' or askforhalo == 'yes'):
        
        fmol = int(input('Enter number of flourines: '))
        clmol = int(input('Enter number of chlorines: '))
        bmol = int(input('Enter number of bromines: '))
        imol = int(input('Enter nunber of iodines: '))

    askforalc = input('Are there any alcohol groups?: ')

    if (askforalc == 'Yes' or askforalc == 'yes'):

        alcmol = int(input('Enter number of alcohol groups: '))

    askforacid = input('Are there any carboxylic acid groups?: ')

    if (askforacid == 'Yes' or askforacid == 'yes'):

        carbox = True

        acidmol = int(input('Enter number of carboxylic acid groups: '))

    if (askforacid == 'No' or askforacid == 'no'):

        acidmol = 0
        
    cmol = (cmol - bcmol)
    hmol = (hmol - bhmol)
    hmol += brantotal

    # HYDROCARBONS

    if (cmol == 1 and hmol == (cmol * 2) + 2):

        hydrocarbon = 'methane'

    if (cmol == 2 and hmol == (cmol * 2) + 2):

        hydrocarbon = 'ethane'

    if (cmol == 3 and hmol == (cmol * 2) + 2):

        hydrocarbon = 'propane'

    if (cmol == 4 and hmol == (cmol * 2) + 2):

        hydrocarbon = 'butane'

    if (cmol == 5 and hmol == (cmol * 2) + 2):

        hydrocarbon = 'pentane'

    if (cmol == 2 and hmol == (cmol * 2)):

        hydrocarbon = 'ethene'

    if (cmol == 3 and hmol == (cmol * 2)):

        hydrocarbon = 'propene'

    if (cmol == 4 and hmol == (cmol * 2)):

        hydrocarbon = 'butene'

    if (cmol == 5 and hmol == (cmol * 2)):

        hydrocarbon = 'pentene'

    # BRANCHED GROUPS

    if (bcmol == 1 and bhmol == 3):

        branch = 'methyl'

    elif (bcmol == 2 and bhmol == 5):

        branch = 'ethyl'

    elif (bcmol == 2 and bhmol == 6):

        branch = 'dimethyl'

    elif (bcmol == 2 and bhmol == 10):

        branch = 'diethyl'

    else:

        branch = ''

    # HALOGENS

    # FLOURINE

    if (fmol == 1):

        fhalo = 'fluoro'

    if (fmol == 2):

        fhalo = 'difluoro'

    if (fmol == 3):

        fhalo = 'trifluoro'

    # CHLORINE

    if (clmol == 1):

        clhalo = 'chloro'

    if (clmol == 2):

        clhalo = 'dichloro'

    if (clmol == 3):

        clhalo = 'trichloro'

    # BROMINE

    if (bmol == 1):

        bhalo = 'bromo'

    if (bmol == 2):

        bhalo = 'dibromo'

    if (bmol == 3):

        bhalo = 'tribromo'
        
    # IODINE

    if (imol == 1):

        ihalo = 'iodo'

    if (imol == 2):

        ihalo = 'diiodo'

    if (imol == 3):

        ihalo = 'triiodo'

    # ALCOHOL

    if (alcmol == 1 and carbox == False and hydrocarbon == 'methane'):

        hydrocarbon = 'methanol'

    if (alcmol == 2 and carbox == False and hydrocarbon == 'methane'):

        hydrocarbon = 'methanediol'

    if (alcmol == 1 and carbox == False and hydrocarbon == 'ethane'):

        hydrocarbon = 'ethanol'

    if (alcmol == 2 and carbox == False and hydrocarbon == 'ethane'):

        hydrocarbon = 'ethanediol'

    if (alcmol == 1 and carbox == False and hydrocarbon == 'propane'):

        hydrocarbon = 'propanol'

    if (alcmol == 2 and carbox == False and hydrocarbon == 'propane'):

        hydrocarbon = 'propanediol'

    if (alcmol == 1 and carbox == False and hydrocarbon == 'butane'):

        hydrocarbon = 'butanol'

    if (alcmol == 2 and carbox == False and hydrocarbon == 'butane'):

        hydrocarbon = 'butanediol'

    if (alcmol == 1 and carbox == True):

        hydroxy = 'hydroxy'

    if (alcmol == 2 and carbox == True):

        hydroxy = 'dihydroxy'

    # CARBOXYLIC ACID

    if (acidmol == 1 and hydrocarbon == 'methane'):

        carhydrocarbon = 'methanoic acid'

    if (acidmol == 1 and hydrocarbon == 'ethane' or hydrocarbon == 'ethene'):

        carhydrocarbon = 'ethanoic acid'

    if (acidmol == 1 and hydrocarbon == 'propane' or hydrocarbon == 'propene'):

        carhydrocarbon = 'propanoic acid'

    if (acidmol == 1 and hydrocarbon == 'butane' or hydrocarbon == 'butene'):

        carhydrocarbon = 'butanoic acid'


    # IDENTIFICATION

    if (cmol < 1 or hmol != (cmol * 2) and hmol != ((cmol * 2) + 2)):

        valid = False

        print('This molecule does not exist.')

    if (valid == True and acidmol == 0):

        print('The molecule is', bhalo + clhalo + fhalo + hydroxy + ihalo + branch + hydrocarbon + '.')

    if (valid == True and acidmol >= 1):

        print('The molecule is', bhalo + clhalo + fhalo + hydroxy + ihalo + branch + carhydrocarbon + '.')

        
