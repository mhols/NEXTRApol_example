import inspect
import nextrapol as nx
from dotenv import load_dotenv

import nextrapol.units as un
import nextrapol.continuum as continuum




class SettingsGammaequNarval(nx.settings_narval.SettingsReferenceNarval):
    IS_REFERENCE = False
    VOIE_METHOD = "OPTIMAL_EXTRACT" #SUM_DIVIDE_CENTRALROW"

    BIG_PSEUDO_FLAT = True # do not use the BIG_PSEUDO_FLAT

    ORDERS = list(range(24, 57))

    DELTA_VRAD_COMMON_GRID = 0.5 * un.KM / un.S

    CONTINUUM_METHOD_CLASS = continuum.GlobalMaskedContinuum
    FLUX_LIMIT = 250 * nx.settings_narval.SettingsReferenceNarval.ADU_FACTOR
    ORDER_LIMIT_THRESHOLD_LAB =  FLUX_LIMIT
    ORDER_LIMIT_THRESHOLD_GAG =  FLUX_LIMIT

def get_kwargs():
    """
    convenient shortcut
    """
    return SettingsGammaequNarval.get_kwargs()
