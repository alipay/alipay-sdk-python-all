#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinDataserviceRegiongroupMatchModel(object):

    def __init__(self):
        self._crop_code = None
        self._growth_strength = None
        self._is_certain_risk = None
        self._is_growth_warn = None
        self._is_harvested = None
        self._is_high_temperature_risk = None
        self._is_low_temperature_risk = None
        self._is_rainstorm_risk = None
        self._is_soil_moisture_risk = None
        self._need_crops_count_only = None
        self._region_group_codes = None

    @property
    def crop_code(self):
        return self._crop_code

    @crop_code.setter
    def crop_code(self, value):
        self._crop_code = value
    @property
    def growth_strength(self):
        return self._growth_strength

    @growth_strength.setter
    def growth_strength(self, value):
        self._growth_strength = value
    @property
    def is_certain_risk(self):
        return self._is_certain_risk

    @is_certain_risk.setter
    def is_certain_risk(self, value):
        self._is_certain_risk = value
    @property
    def is_growth_warn(self):
        return self._is_growth_warn

    @is_growth_warn.setter
    def is_growth_warn(self, value):
        self._is_growth_warn = value
    @property
    def is_harvested(self):
        return self._is_harvested

    @is_harvested.setter
    def is_harvested(self, value):
        self._is_harvested = value
    @property
    def is_high_temperature_risk(self):
        return self._is_high_temperature_risk

    @is_high_temperature_risk.setter
    def is_high_temperature_risk(self, value):
        self._is_high_temperature_risk = value
    @property
    def is_low_temperature_risk(self):
        return self._is_low_temperature_risk

    @is_low_temperature_risk.setter
    def is_low_temperature_risk(self, value):
        self._is_low_temperature_risk = value
    @property
    def is_rainstorm_risk(self):
        return self._is_rainstorm_risk

    @is_rainstorm_risk.setter
    def is_rainstorm_risk(self, value):
        self._is_rainstorm_risk = value
    @property
    def is_soil_moisture_risk(self):
        return self._is_soil_moisture_risk

    @is_soil_moisture_risk.setter
    def is_soil_moisture_risk(self, value):
        self._is_soil_moisture_risk = value
    @property
    def need_crops_count_only(self):
        return self._need_crops_count_only

    @need_crops_count_only.setter
    def need_crops_count_only(self, value):
        self._need_crops_count_only = value
    @property
    def region_group_codes(self):
        return self._region_group_codes

    @region_group_codes.setter
    def region_group_codes(self, value):
        if isinstance(value, list):
            self._region_group_codes = list()
            for i in value:
                self._region_group_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.crop_code:
            if hasattr(self.crop_code, 'to_alipay_dict'):
                params['crop_code'] = self.crop_code.to_alipay_dict()
            else:
                params['crop_code'] = self.crop_code
        if self.growth_strength:
            if hasattr(self.growth_strength, 'to_alipay_dict'):
                params['growth_strength'] = self.growth_strength.to_alipay_dict()
            else:
                params['growth_strength'] = self.growth_strength
        if self.is_certain_risk:
            if hasattr(self.is_certain_risk, 'to_alipay_dict'):
                params['is_certain_risk'] = self.is_certain_risk.to_alipay_dict()
            else:
                params['is_certain_risk'] = self.is_certain_risk
        if self.is_growth_warn:
            if hasattr(self.is_growth_warn, 'to_alipay_dict'):
                params['is_growth_warn'] = self.is_growth_warn.to_alipay_dict()
            else:
                params['is_growth_warn'] = self.is_growth_warn
        if self.is_harvested:
            if hasattr(self.is_harvested, 'to_alipay_dict'):
                params['is_harvested'] = self.is_harvested.to_alipay_dict()
            else:
                params['is_harvested'] = self.is_harvested
        if self.is_high_temperature_risk:
            if hasattr(self.is_high_temperature_risk, 'to_alipay_dict'):
                params['is_high_temperature_risk'] = self.is_high_temperature_risk.to_alipay_dict()
            else:
                params['is_high_temperature_risk'] = self.is_high_temperature_risk
        if self.is_low_temperature_risk:
            if hasattr(self.is_low_temperature_risk, 'to_alipay_dict'):
                params['is_low_temperature_risk'] = self.is_low_temperature_risk.to_alipay_dict()
            else:
                params['is_low_temperature_risk'] = self.is_low_temperature_risk
        if self.is_rainstorm_risk:
            if hasattr(self.is_rainstorm_risk, 'to_alipay_dict'):
                params['is_rainstorm_risk'] = self.is_rainstorm_risk.to_alipay_dict()
            else:
                params['is_rainstorm_risk'] = self.is_rainstorm_risk
        if self.is_soil_moisture_risk:
            if hasattr(self.is_soil_moisture_risk, 'to_alipay_dict'):
                params['is_soil_moisture_risk'] = self.is_soil_moisture_risk.to_alipay_dict()
            else:
                params['is_soil_moisture_risk'] = self.is_soil_moisture_risk
        if self.need_crops_count_only:
            if hasattr(self.need_crops_count_only, 'to_alipay_dict'):
                params['need_crops_count_only'] = self.need_crops_count_only.to_alipay_dict()
            else:
                params['need_crops_count_only'] = self.need_crops_count_only
        if self.region_group_codes:
            if isinstance(self.region_group_codes, list):
                for i in range(0, len(self.region_group_codes)):
                    element = self.region_group_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_group_codes[i] = element.to_alipay_dict()
            if hasattr(self.region_group_codes, 'to_alipay_dict'):
                params['region_group_codes'] = self.region_group_codes.to_alipay_dict()
            else:
                params['region_group_codes'] = self.region_group_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinDataserviceRegiongroupMatchModel()
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'growth_strength' in d:
            o.growth_strength = d['growth_strength']
        if 'is_certain_risk' in d:
            o.is_certain_risk = d['is_certain_risk']
        if 'is_growth_warn' in d:
            o.is_growth_warn = d['is_growth_warn']
        if 'is_harvested' in d:
            o.is_harvested = d['is_harvested']
        if 'is_high_temperature_risk' in d:
            o.is_high_temperature_risk = d['is_high_temperature_risk']
        if 'is_low_temperature_risk' in d:
            o.is_low_temperature_risk = d['is_low_temperature_risk']
        if 'is_rainstorm_risk' in d:
            o.is_rainstorm_risk = d['is_rainstorm_risk']
        if 'is_soil_moisture_risk' in d:
            o.is_soil_moisture_risk = d['is_soil_moisture_risk']
        if 'need_crops_count_only' in d:
            o.need_crops_count_only = d['need_crops_count_only']
        if 'region_group_codes' in d:
            o.region_group_codes = d['region_group_codes']
        return o


