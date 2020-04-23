# pyextremes, Extreme Value Analysis in Python
# Copyright (C), 2020 Georgii Bocharov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging

import pandas as pd

from pyextremes.models.emcee.genextreme import Genextreme
from pyextremes.models.emcee.genpareto import Genpareto

logger = logging.getLogger(__name__)


def get_distribution(
        distribution: str,
        extremes: pd.Series,
):
    if distribution == 'genextreme':
        return Genextreme(extremes=extremes)
    elif distribution == 'genpareto':
        return Genpareto(extremes=extremes)
    else:
        raise NotImplementedError(f'\'{distribution}\' distribution is not implemented for the \'emcee\' model')