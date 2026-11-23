#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegisterNumber import RegisterNumber


class RegisterClinic(object):

    def __init__(self):
        self._number_list = None
        self._register_date = None
        self._register_id_list = None
        self._weekday = None

    @property
    def number_list(self):
        return self._number_list

    @number_list.setter
    def number_list(self, value):
        if isinstance(value, list):
            self._number_list = list()
            for i in value:
                if isinstance(i, RegisterNumber):
                    self._number_list.append(i)
                else:
                    self._number_list.append(RegisterNumber.from_alipay_dict(i))
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def register_id_list(self):
        return self._register_id_list

    @register_id_list.setter
    def register_id_list(self, value):
        if isinstance(value, list):
            self._register_id_list = list()
            for i in value:
                self._register_id_list.append(i)
    @property
    def weekday(self):
        return self._weekday

    @weekday.setter
    def weekday(self, value):
        self._weekday = value


    def to_alipay_dict(self):
        params = dict()
        if self.number_list:
            if isinstance(self.number_list, list):
                for i in range(0, len(self.number_list)):
                    element = self.number_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.number_list[i] = element.to_alipay_dict()
            if hasattr(self.number_list, 'to_alipay_dict'):
                params['number_list'] = self.number_list.to_alipay_dict()
            else:
                params['number_list'] = self.number_list
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.register_id_list:
            if isinstance(self.register_id_list, list):
                for i in range(0, len(self.register_id_list)):
                    element = self.register_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.register_id_list[i] = element.to_alipay_dict()
            if hasattr(self.register_id_list, 'to_alipay_dict'):
                params['register_id_list'] = self.register_id_list.to_alipay_dict()
            else:
                params['register_id_list'] = self.register_id_list
        if self.weekday:
            if hasattr(self.weekday, 'to_alipay_dict'):
                params['weekday'] = self.weekday.to_alipay_dict()
            else:
                params['weekday'] = self.weekday
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterClinic()
        if 'number_list' in d:
            o.number_list = d['number_list']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'register_id_list' in d:
            o.register_id_list = d['register_id_list']
        if 'weekday' in d:
            o.weekday = d['weekday']
        return o


