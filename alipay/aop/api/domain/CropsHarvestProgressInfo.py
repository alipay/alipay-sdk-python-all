#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CropsHarvestProgressInfo(object):

    def __init__(self):
        self._actual_date = None
        self._addition_info = None
        self._crop_code = None
        self._harvest_progress_value = None
        self._harvested_area = None
        self._total_area = None

    @property
    def actual_date(self):
        return self._actual_date

    @actual_date.setter
    def actual_date(self, value):
        self._actual_date = value
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
    def harvest_progress_value(self):
        return self._harvest_progress_value

    @harvest_progress_value.setter
    def harvest_progress_value(self, value):
        self._harvest_progress_value = value
    @property
    def harvested_area(self):
        return self._harvested_area

    @harvested_area.setter
    def harvested_area(self, value):
        self._harvested_area = value
    @property
    def total_area(self):
        return self._total_area

    @total_area.setter
    def total_area(self, value):
        self._total_area = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_date:
            if hasattr(self.actual_date, 'to_alipay_dict'):
                params['actual_date'] = self.actual_date.to_alipay_dict()
            else:
                params['actual_date'] = self.actual_date
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
        if self.harvest_progress_value:
            if hasattr(self.harvest_progress_value, 'to_alipay_dict'):
                params['harvest_progress_value'] = self.harvest_progress_value.to_alipay_dict()
            else:
                params['harvest_progress_value'] = self.harvest_progress_value
        if self.harvested_area:
            if hasattr(self.harvested_area, 'to_alipay_dict'):
                params['harvested_area'] = self.harvested_area.to_alipay_dict()
            else:
                params['harvested_area'] = self.harvested_area
        if self.total_area:
            if hasattr(self.total_area, 'to_alipay_dict'):
                params['total_area'] = self.total_area.to_alipay_dict()
            else:
                params['total_area'] = self.total_area
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsHarvestProgressInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'harvest_progress_value' in d:
            o.harvest_progress_value = d['harvest_progress_value']
        if 'harvested_area' in d:
            o.harvested_area = d['harvested_area']
        if 'total_area' in d:
            o.total_area = d['total_area']
        return o


