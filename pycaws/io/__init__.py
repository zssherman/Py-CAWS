"""
================
Input and output
================

Functions to read, process and write stage and weather data.

    cso_output
    cso_preparation
    cso_aggregation
    stage_output
    weather_output
    load_caws_site
    load_predict_site
    save_predict_site

"""

from .cso_processing import cso_output
from .cso_processing import cso_preparation, cso_aggregation
from .stage_processing import stage_output
from .weather_processing import weather_output
from .variable_importance import load_caws_site, load_predict_site
from .variable_importance import save_predict_site

__all__ = [s for s in dir() if not s.startswith('_')]
