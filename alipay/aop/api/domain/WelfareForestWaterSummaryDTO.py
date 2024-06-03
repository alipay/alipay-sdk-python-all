#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WelfareForestWaterSummaryDTO(object):

    def __init__(self):
        self._plant_sum = None
        self._water_count = None
        self._water_people_count = None
        self._water_sum = None

    @property
    def plant_sum(self):
        return self._plant_sum

    @plant_sum.setter
    def plant_sum(self, value):
        self._plant_sum = value
    @property
    def water_count(self):
        return self._water_count

    @water_count.setter
    def water_count(self, value):
        self._water_count = value
    @property
    def water_people_count(self):
        return self._water_people_count

    @water_people_count.setter
    def water_people_count(self, value):
        self._water_people_count = value
    @property
    def water_sum(self):
        return self._water_sum

    @water_sum.setter
    def water_sum(self, value):
        self._water_sum = value


    def to_alipay_dict(self):
        params = dict()
        if self.plant_sum:
            if hasattr(self.plant_sum, 'to_alipay_dict'):
                params['plant_sum'] = self.plant_sum.to_alipay_dict()
            else:
                params['plant_sum'] = self.plant_sum
        if self.water_count:
            if hasattr(self.water_count, 'to_alipay_dict'):
                params['water_count'] = self.water_count.to_alipay_dict()
            else:
                params['water_count'] = self.water_count
        if self.water_people_count:
            if hasattr(self.water_people_count, 'to_alipay_dict'):
                params['water_people_count'] = self.water_people_count.to_alipay_dict()
            else:
                params['water_people_count'] = self.water_people_count
        if self.water_sum:
            if hasattr(self.water_sum, 'to_alipay_dict'):
                params['water_sum'] = self.water_sum.to_alipay_dict()
            else:
                params['water_sum'] = self.water_sum
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareForestWaterSummaryDTO()
        if 'plant_sum' in d:
            o.plant_sum = d['plant_sum']
        if 'water_count' in d:
            o.water_count = d['water_count']
        if 'water_people_count' in d:
            o.water_people_count = d['water_people_count']
        if 'water_sum' in d:
            o.water_sum = d['water_sum']
        return o


