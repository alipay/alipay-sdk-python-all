#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CropsStatisticsInfo(object):

    def __init__(self):
        self._addition_info = None
        self._crop_code = None
        self._drought_risk_plot_count = None
        self._estimate_harvest_time_max = None
        self._estimate_harvest_time_min = None
        self._growth_general_area_sum = None
        self._growth_general_plot_count = None
        self._growth_stronger_area_sum = None
        self._growth_stronger_plot_count = None
        self._growth_strongest_area_sum = None
        self._growth_strongest_plot_count = None
        self._growth_weaker_area_sum = None
        self._growth_weaker_plot_count = None
        self._growth_weakest_area_sum = None
        self._growth_weakest_plot_count = None
        self._harvest_progress_value = None
        self._harvested_area_sum = None
        self._high_temp_risk_plot_count = None
        self._low_temp_risk_plot_count = None
        self._maturity_plot_count = None
        self._not_harvested_area_sum = None
        self._planting_area_sum = None
        self._plot_area_sum = None
        self._plot_count = None
        self._rainstorm_risk_plot_count = None
        self._region_codes = None
        self._soil_moisture_risk_plot_count = None
        self._total_area_sum = None
        self._total_yield_sum = None

    @property
    def addition_info(self):
        return self._addition_info

    @addition_info.setter
    def addition_info(self, value):
        self._addition_info = value
    @property
    def crop_code(self):
        return self._crop_code

    @crop_code.setter
    def crop_code(self, value):
        self._crop_code = value
    @property
    def drought_risk_plot_count(self):
        return self._drought_risk_plot_count

    @drought_risk_plot_count.setter
    def drought_risk_plot_count(self, value):
        self._drought_risk_plot_count = value
    @property
    def estimate_harvest_time_max(self):
        return self._estimate_harvest_time_max

    @estimate_harvest_time_max.setter
    def estimate_harvest_time_max(self, value):
        self._estimate_harvest_time_max = value
    @property
    def estimate_harvest_time_min(self):
        return self._estimate_harvest_time_min

    @estimate_harvest_time_min.setter
    def estimate_harvest_time_min(self, value):
        self._estimate_harvest_time_min = value
    @property
    def growth_general_area_sum(self):
        return self._growth_general_area_sum

    @growth_general_area_sum.setter
    def growth_general_area_sum(self, value):
        self._growth_general_area_sum = value
    @property
    def growth_general_plot_count(self):
        return self._growth_general_plot_count

    @growth_general_plot_count.setter
    def growth_general_plot_count(self, value):
        self._growth_general_plot_count = value
    @property
    def growth_stronger_area_sum(self):
        return self._growth_stronger_area_sum

    @growth_stronger_area_sum.setter
    def growth_stronger_area_sum(self, value):
        self._growth_stronger_area_sum = value
    @property
    def growth_stronger_plot_count(self):
        return self._growth_stronger_plot_count

    @growth_stronger_plot_count.setter
    def growth_stronger_plot_count(self, value):
        self._growth_stronger_plot_count = value
    @property
    def growth_strongest_area_sum(self):
        return self._growth_strongest_area_sum

    @growth_strongest_area_sum.setter
    def growth_strongest_area_sum(self, value):
        self._growth_strongest_area_sum = value
    @property
    def growth_strongest_plot_count(self):
        return self._growth_strongest_plot_count

    @growth_strongest_plot_count.setter
    def growth_strongest_plot_count(self, value):
        self._growth_strongest_plot_count = value
    @property
    def growth_weaker_area_sum(self):
        return self._growth_weaker_area_sum

    @growth_weaker_area_sum.setter
    def growth_weaker_area_sum(self, value):
        self._growth_weaker_area_sum = value
    @property
    def growth_weaker_plot_count(self):
        return self._growth_weaker_plot_count

    @growth_weaker_plot_count.setter
    def growth_weaker_plot_count(self, value):
        self._growth_weaker_plot_count = value
    @property
    def growth_weakest_area_sum(self):
        return self._growth_weakest_area_sum

    @growth_weakest_area_sum.setter
    def growth_weakest_area_sum(self, value):
        self._growth_weakest_area_sum = value
    @property
    def growth_weakest_plot_count(self):
        return self._growth_weakest_plot_count

    @growth_weakest_plot_count.setter
    def growth_weakest_plot_count(self, value):
        self._growth_weakest_plot_count = value
    @property
    def harvest_progress_value(self):
        return self._harvest_progress_value

    @harvest_progress_value.setter
    def harvest_progress_value(self, value):
        self._harvest_progress_value = value
    @property
    def harvested_area_sum(self):
        return self._harvested_area_sum

    @harvested_area_sum.setter
    def harvested_area_sum(self, value):
        self._harvested_area_sum = value
    @property
    def high_temp_risk_plot_count(self):
        return self._high_temp_risk_plot_count

    @high_temp_risk_plot_count.setter
    def high_temp_risk_plot_count(self, value):
        self._high_temp_risk_plot_count = value
    @property
    def low_temp_risk_plot_count(self):
        return self._low_temp_risk_plot_count

    @low_temp_risk_plot_count.setter
    def low_temp_risk_plot_count(self, value):
        self._low_temp_risk_plot_count = value
    @property
    def maturity_plot_count(self):
        return self._maturity_plot_count

    @maturity_plot_count.setter
    def maturity_plot_count(self, value):
        self._maturity_plot_count = value
    @property
    def not_harvested_area_sum(self):
        return self._not_harvested_area_sum

    @not_harvested_area_sum.setter
    def not_harvested_area_sum(self, value):
        self._not_harvested_area_sum = value
    @property
    def planting_area_sum(self):
        return self._planting_area_sum

    @planting_area_sum.setter
    def planting_area_sum(self, value):
        self._planting_area_sum = value
    @property
    def plot_area_sum(self):
        return self._plot_area_sum

    @plot_area_sum.setter
    def plot_area_sum(self, value):
        self._plot_area_sum = value
    @property
    def plot_count(self):
        return self._plot_count

    @plot_count.setter
    def plot_count(self, value):
        self._plot_count = value
    @property
    def rainstorm_risk_plot_count(self):
        return self._rainstorm_risk_plot_count

    @rainstorm_risk_plot_count.setter
    def rainstorm_risk_plot_count(self, value):
        self._rainstorm_risk_plot_count = value
    @property
    def region_codes(self):
        return self._region_codes

    @region_codes.setter
    def region_codes(self, value):
        if isinstance(value, list):
            self._region_codes = list()
            for i in value:
                self._region_codes.append(i)
    @property
    def soil_moisture_risk_plot_count(self):
        return self._soil_moisture_risk_plot_count

    @soil_moisture_risk_plot_count.setter
    def soil_moisture_risk_plot_count(self, value):
        self._soil_moisture_risk_plot_count = value
    @property
    def total_area_sum(self):
        return self._total_area_sum

    @total_area_sum.setter
    def total_area_sum(self, value):
        self._total_area_sum = value
    @property
    def total_yield_sum(self):
        return self._total_yield_sum

    @total_yield_sum.setter
    def total_yield_sum(self, value):
        self._total_yield_sum = value


    def to_alipay_dict(self):
        params = dict()
        if self.addition_info:
            if hasattr(self.addition_info, 'to_alipay_dict'):
                params['addition_info'] = self.addition_info.to_alipay_dict()
            else:
                params['addition_info'] = self.addition_info
        if self.crop_code:
            if hasattr(self.crop_code, 'to_alipay_dict'):
                params['crop_code'] = self.crop_code.to_alipay_dict()
            else:
                params['crop_code'] = self.crop_code
        if self.drought_risk_plot_count:
            if hasattr(self.drought_risk_plot_count, 'to_alipay_dict'):
                params['drought_risk_plot_count'] = self.drought_risk_plot_count.to_alipay_dict()
            else:
                params['drought_risk_plot_count'] = self.drought_risk_plot_count
        if self.estimate_harvest_time_max:
            if hasattr(self.estimate_harvest_time_max, 'to_alipay_dict'):
                params['estimate_harvest_time_max'] = self.estimate_harvest_time_max.to_alipay_dict()
            else:
                params['estimate_harvest_time_max'] = self.estimate_harvest_time_max
        if self.estimate_harvest_time_min:
            if hasattr(self.estimate_harvest_time_min, 'to_alipay_dict'):
                params['estimate_harvest_time_min'] = self.estimate_harvest_time_min.to_alipay_dict()
            else:
                params['estimate_harvest_time_min'] = self.estimate_harvest_time_min
        if self.growth_general_area_sum:
            if hasattr(self.growth_general_area_sum, 'to_alipay_dict'):
                params['growth_general_area_sum'] = self.growth_general_area_sum.to_alipay_dict()
            else:
                params['growth_general_area_sum'] = self.growth_general_area_sum
        if self.growth_general_plot_count:
            if hasattr(self.growth_general_plot_count, 'to_alipay_dict'):
                params['growth_general_plot_count'] = self.growth_general_plot_count.to_alipay_dict()
            else:
                params['growth_general_plot_count'] = self.growth_general_plot_count
        if self.growth_stronger_area_sum:
            if hasattr(self.growth_stronger_area_sum, 'to_alipay_dict'):
                params['growth_stronger_area_sum'] = self.growth_stronger_area_sum.to_alipay_dict()
            else:
                params['growth_stronger_area_sum'] = self.growth_stronger_area_sum
        if self.growth_stronger_plot_count:
            if hasattr(self.growth_stronger_plot_count, 'to_alipay_dict'):
                params['growth_stronger_plot_count'] = self.growth_stronger_plot_count.to_alipay_dict()
            else:
                params['growth_stronger_plot_count'] = self.growth_stronger_plot_count
        if self.growth_strongest_area_sum:
            if hasattr(self.growth_strongest_area_sum, 'to_alipay_dict'):
                params['growth_strongest_area_sum'] = self.growth_strongest_area_sum.to_alipay_dict()
            else:
                params['growth_strongest_area_sum'] = self.growth_strongest_area_sum
        if self.growth_strongest_plot_count:
            if hasattr(self.growth_strongest_plot_count, 'to_alipay_dict'):
                params['growth_strongest_plot_count'] = self.growth_strongest_plot_count.to_alipay_dict()
            else:
                params['growth_strongest_plot_count'] = self.growth_strongest_plot_count
        if self.growth_weaker_area_sum:
            if hasattr(self.growth_weaker_area_sum, 'to_alipay_dict'):
                params['growth_weaker_area_sum'] = self.growth_weaker_area_sum.to_alipay_dict()
            else:
                params['growth_weaker_area_sum'] = self.growth_weaker_area_sum
        if self.growth_weaker_plot_count:
            if hasattr(self.growth_weaker_plot_count, 'to_alipay_dict'):
                params['growth_weaker_plot_count'] = self.growth_weaker_plot_count.to_alipay_dict()
            else:
                params['growth_weaker_plot_count'] = self.growth_weaker_plot_count
        if self.growth_weakest_area_sum:
            if hasattr(self.growth_weakest_area_sum, 'to_alipay_dict'):
                params['growth_weakest_area_sum'] = self.growth_weakest_area_sum.to_alipay_dict()
            else:
                params['growth_weakest_area_sum'] = self.growth_weakest_area_sum
        if self.growth_weakest_plot_count:
            if hasattr(self.growth_weakest_plot_count, 'to_alipay_dict'):
                params['growth_weakest_plot_count'] = self.growth_weakest_plot_count.to_alipay_dict()
            else:
                params['growth_weakest_plot_count'] = self.growth_weakest_plot_count
        if self.harvest_progress_value:
            if hasattr(self.harvest_progress_value, 'to_alipay_dict'):
                params['harvest_progress_value'] = self.harvest_progress_value.to_alipay_dict()
            else:
                params['harvest_progress_value'] = self.harvest_progress_value
        if self.harvested_area_sum:
            if hasattr(self.harvested_area_sum, 'to_alipay_dict'):
                params['harvested_area_sum'] = self.harvested_area_sum.to_alipay_dict()
            else:
                params['harvested_area_sum'] = self.harvested_area_sum
        if self.high_temp_risk_plot_count:
            if hasattr(self.high_temp_risk_plot_count, 'to_alipay_dict'):
                params['high_temp_risk_plot_count'] = self.high_temp_risk_plot_count.to_alipay_dict()
            else:
                params['high_temp_risk_plot_count'] = self.high_temp_risk_plot_count
        if self.low_temp_risk_plot_count:
            if hasattr(self.low_temp_risk_plot_count, 'to_alipay_dict'):
                params['low_temp_risk_plot_count'] = self.low_temp_risk_plot_count.to_alipay_dict()
            else:
                params['low_temp_risk_plot_count'] = self.low_temp_risk_plot_count
        if self.maturity_plot_count:
            if hasattr(self.maturity_plot_count, 'to_alipay_dict'):
                params['maturity_plot_count'] = self.maturity_plot_count.to_alipay_dict()
            else:
                params['maturity_plot_count'] = self.maturity_plot_count
        if self.not_harvested_area_sum:
            if hasattr(self.not_harvested_area_sum, 'to_alipay_dict'):
                params['not_harvested_area_sum'] = self.not_harvested_area_sum.to_alipay_dict()
            else:
                params['not_harvested_area_sum'] = self.not_harvested_area_sum
        if self.planting_area_sum:
            if hasattr(self.planting_area_sum, 'to_alipay_dict'):
                params['planting_area_sum'] = self.planting_area_sum.to_alipay_dict()
            else:
                params['planting_area_sum'] = self.planting_area_sum
        if self.plot_area_sum:
            if hasattr(self.plot_area_sum, 'to_alipay_dict'):
                params['plot_area_sum'] = self.plot_area_sum.to_alipay_dict()
            else:
                params['plot_area_sum'] = self.plot_area_sum
        if self.plot_count:
            if hasattr(self.plot_count, 'to_alipay_dict'):
                params['plot_count'] = self.plot_count.to_alipay_dict()
            else:
                params['plot_count'] = self.plot_count
        if self.rainstorm_risk_plot_count:
            if hasattr(self.rainstorm_risk_plot_count, 'to_alipay_dict'):
                params['rainstorm_risk_plot_count'] = self.rainstorm_risk_plot_count.to_alipay_dict()
            else:
                params['rainstorm_risk_plot_count'] = self.rainstorm_risk_plot_count
        if self.region_codes:
            if isinstance(self.region_codes, list):
                for i in range(0, len(self.region_codes)):
                    element = self.region_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_codes[i] = element.to_alipay_dict()
            if hasattr(self.region_codes, 'to_alipay_dict'):
                params['region_codes'] = self.region_codes.to_alipay_dict()
            else:
                params['region_codes'] = self.region_codes
        if self.soil_moisture_risk_plot_count:
            if hasattr(self.soil_moisture_risk_plot_count, 'to_alipay_dict'):
                params['soil_moisture_risk_plot_count'] = self.soil_moisture_risk_plot_count.to_alipay_dict()
            else:
                params['soil_moisture_risk_plot_count'] = self.soil_moisture_risk_plot_count
        if self.total_area_sum:
            if hasattr(self.total_area_sum, 'to_alipay_dict'):
                params['total_area_sum'] = self.total_area_sum.to_alipay_dict()
            else:
                params['total_area_sum'] = self.total_area_sum
        if self.total_yield_sum:
            if hasattr(self.total_yield_sum, 'to_alipay_dict'):
                params['total_yield_sum'] = self.total_yield_sum.to_alipay_dict()
            else:
                params['total_yield_sum'] = self.total_yield_sum
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsStatisticsInfo()
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'drought_risk_plot_count' in d:
            o.drought_risk_plot_count = d['drought_risk_plot_count']
        if 'estimate_harvest_time_max' in d:
            o.estimate_harvest_time_max = d['estimate_harvest_time_max']
        if 'estimate_harvest_time_min' in d:
            o.estimate_harvest_time_min = d['estimate_harvest_time_min']
        if 'growth_general_area_sum' in d:
            o.growth_general_area_sum = d['growth_general_area_sum']
        if 'growth_general_plot_count' in d:
            o.growth_general_plot_count = d['growth_general_plot_count']
        if 'growth_stronger_area_sum' in d:
            o.growth_stronger_area_sum = d['growth_stronger_area_sum']
        if 'growth_stronger_plot_count' in d:
            o.growth_stronger_plot_count = d['growth_stronger_plot_count']
        if 'growth_strongest_area_sum' in d:
            o.growth_strongest_area_sum = d['growth_strongest_area_sum']
        if 'growth_strongest_plot_count' in d:
            o.growth_strongest_plot_count = d['growth_strongest_plot_count']
        if 'growth_weaker_area_sum' in d:
            o.growth_weaker_area_sum = d['growth_weaker_area_sum']
        if 'growth_weaker_plot_count' in d:
            o.growth_weaker_plot_count = d['growth_weaker_plot_count']
        if 'growth_weakest_area_sum' in d:
            o.growth_weakest_area_sum = d['growth_weakest_area_sum']
        if 'growth_weakest_plot_count' in d:
            o.growth_weakest_plot_count = d['growth_weakest_plot_count']
        if 'harvest_progress_value' in d:
            o.harvest_progress_value = d['harvest_progress_value']
        if 'harvested_area_sum' in d:
            o.harvested_area_sum = d['harvested_area_sum']
        if 'high_temp_risk_plot_count' in d:
            o.high_temp_risk_plot_count = d['high_temp_risk_plot_count']
        if 'low_temp_risk_plot_count' in d:
            o.low_temp_risk_plot_count = d['low_temp_risk_plot_count']
        if 'maturity_plot_count' in d:
            o.maturity_plot_count = d['maturity_plot_count']
        if 'not_harvested_area_sum' in d:
            o.not_harvested_area_sum = d['not_harvested_area_sum']
        if 'planting_area_sum' in d:
            o.planting_area_sum = d['planting_area_sum']
        if 'plot_area_sum' in d:
            o.plot_area_sum = d['plot_area_sum']
        if 'plot_count' in d:
            o.plot_count = d['plot_count']
        if 'rainstorm_risk_plot_count' in d:
            o.rainstorm_risk_plot_count = d['rainstorm_risk_plot_count']
        if 'region_codes' in d:
            o.region_codes = d['region_codes']
        if 'soil_moisture_risk_plot_count' in d:
            o.soil_moisture_risk_plot_count = d['soil_moisture_risk_plot_count']
        if 'total_area_sum' in d:
            o.total_area_sum = d['total_area_sum']
        if 'total_yield_sum' in d:
            o.total_yield_sum = d['total_yield_sum']
        return o


