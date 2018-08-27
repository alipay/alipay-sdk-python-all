#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeInstMode(object):

    def __init__(self):
        self._charge_inst = None
        self._charge_inst_name = None
        self._city = None
        self._province = None

    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def charge_inst_name(self):
        return self._charge_inst_name

    @charge_inst_name.setter
    def charge_inst_name(self, value):
        self._charge_inst_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.charge_inst_name:
            if hasattr(self.charge_inst_name, 'to_alipay_dict'):
                params['charge_inst_name'] = self.charge_inst_name.to_alipay_dict()
            else:
                params['charge_inst_name'] = self.charge_inst_name
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeInstMode()
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'charge_inst_name' in d:
            o.charge_inst_name = d['charge_inst_name']
        if 'city' in d:
            o.city = d['city']
        if 'province' in d:
            o.province = d['province']
        return o


