#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CropsGrowthInfo(object):

    def __init__(self):
        self._actual_date = None
        self._addition_info = None
        self._crop_code = None
        self._general_area = None
        self._strength = None
        self._stronger_area = None
        self._strongest_area = None
        self._warn = None
        self._weaker_area = None
        self._weakest_area = None

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
    def general_area(self):
        return self._general_area

    @general_area.setter
    def general_area(self, value):
        self._general_area = value
    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value
    @property
    def stronger_area(self):
        return self._stronger_area

    @stronger_area.setter
    def stronger_area(self, value):
        self._stronger_area = value
    @property
    def strongest_area(self):
        return self._strongest_area

    @strongest_area.setter
    def strongest_area(self, value):
        self._strongest_area = value
    @property
    def warn(self):
        return self._warn

    @warn.setter
    def warn(self, value):
        self._warn = value
    @property
    def weaker_area(self):
        return self._weaker_area

    @weaker_area.setter
    def weaker_area(self, value):
        self._weaker_area = value
    @property
    def weakest_area(self):
        return self._weakest_area

    @weakest_area.setter
    def weakest_area(self, value):
        self._weakest_area = value


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
        if self.general_area:
            if hasattr(self.general_area, 'to_alipay_dict'):
                params['general_area'] = self.general_area.to_alipay_dict()
            else:
                params['general_area'] = self.general_area
        if self.strength:
            if hasattr(self.strength, 'to_alipay_dict'):
                params['strength'] = self.strength.to_alipay_dict()
            else:
                params['strength'] = self.strength
        if self.stronger_area:
            if hasattr(self.stronger_area, 'to_alipay_dict'):
                params['stronger_area'] = self.stronger_area.to_alipay_dict()
            else:
                params['stronger_area'] = self.stronger_area
        if self.strongest_area:
            if hasattr(self.strongest_area, 'to_alipay_dict'):
                params['strongest_area'] = self.strongest_area.to_alipay_dict()
            else:
                params['strongest_area'] = self.strongest_area
        if self.warn:
            if hasattr(self.warn, 'to_alipay_dict'):
                params['warn'] = self.warn.to_alipay_dict()
            else:
                params['warn'] = self.warn
        if self.weaker_area:
            if hasattr(self.weaker_area, 'to_alipay_dict'):
                params['weaker_area'] = self.weaker_area.to_alipay_dict()
            else:
                params['weaker_area'] = self.weaker_area
        if self.weakest_area:
            if hasattr(self.weakest_area, 'to_alipay_dict'):
                params['weakest_area'] = self.weakest_area.to_alipay_dict()
            else:
                params['weakest_area'] = self.weakest_area
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsGrowthInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'general_area' in d:
            o.general_area = d['general_area']
        if 'strength' in d:
            o.strength = d['strength']
        if 'stronger_area' in d:
            o.stronger_area = d['stronger_area']
        if 'strongest_area' in d:
            o.strongest_area = d['strongest_area']
        if 'warn' in d:
            o.warn = d['warn']
        if 'weaker_area' in d:
            o.weaker_area = d['weaker_area']
        if 'weakest_area' in d:
            o.weakest_area = d['weakest_area']
        return o


