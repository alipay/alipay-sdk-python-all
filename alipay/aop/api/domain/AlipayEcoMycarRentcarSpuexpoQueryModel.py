#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarSpuexpoQueryModel(object):

    def __init__(self):
        self._bizdate = None
        self._car_type = None
        self._city_name = None
        self._page_no = None
        self._page_size = None
        self._veh_name = None

    @property
    def bizdate(self):
        return self._bizdate

    @bizdate.setter
    def bizdate(self, value):
        self._bizdate = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def veh_name(self):
        return self._veh_name

    @veh_name.setter
    def veh_name(self, value):
        self._veh_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bizdate:
            if hasattr(self.bizdate, 'to_alipay_dict'):
                params['bizdate'] = self.bizdate.to_alipay_dict()
            else:
                params['bizdate'] = self.bizdate
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.veh_name:
            if hasattr(self.veh_name, 'to_alipay_dict'):
                params['veh_name'] = self.veh_name.to_alipay_dict()
            else:
                params['veh_name'] = self.veh_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarRentcarSpuexpoQueryModel()
        if 'bizdate' in d:
            o.bizdate = d['bizdate']
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'veh_name' in d:
            o.veh_name = d['veh_name']
        return o


