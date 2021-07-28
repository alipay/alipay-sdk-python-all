#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandRegistrationInfo(object):

    def __init__(self):
        self._end_date = None
        self._reg_materials = None
        self._reg_number = None
        self._registrant = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def reg_materials(self):
        return self._reg_materials

    @reg_materials.setter
    def reg_materials(self, value):
        if isinstance(value, list):
            self._reg_materials = list()
            for i in value:
                self._reg_materials.append(i)
    @property
    def reg_number(self):
        return self._reg_number

    @reg_number.setter
    def reg_number(self, value):
        self._reg_number = value
    @property
    def registrant(self):
        return self._registrant

    @registrant.setter
    def registrant(self, value):
        self._registrant = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.reg_materials:
            if isinstance(self.reg_materials, list):
                for i in range(0, len(self.reg_materials)):
                    element = self.reg_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reg_materials[i] = element.to_alipay_dict()
            if hasattr(self.reg_materials, 'to_alipay_dict'):
                params['reg_materials'] = self.reg_materials.to_alipay_dict()
            else:
                params['reg_materials'] = self.reg_materials
        if self.reg_number:
            if hasattr(self.reg_number, 'to_alipay_dict'):
                params['reg_number'] = self.reg_number.to_alipay_dict()
            else:
                params['reg_number'] = self.reg_number
        if self.registrant:
            if hasattr(self.registrant, 'to_alipay_dict'):
                params['registrant'] = self.registrant.to_alipay_dict()
            else:
                params['registrant'] = self.registrant
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandRegistrationInfo()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'reg_materials' in d:
            o.reg_materials = d['reg_materials']
        if 'reg_number' in d:
            o.reg_number = d['reg_number']
        if 'registrant' in d:
            o.registrant = d['registrant']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


