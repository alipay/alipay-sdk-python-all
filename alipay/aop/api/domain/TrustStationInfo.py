#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrustStationInfo(object):

    def __init__(self):
        self._construction = None
        self._demand_load_max = None
        self._electric_account = None
        self._peak_shaving_load_max = None
        self._service_tel = None
        self._transformer_load_max = None
        self._transformer_load_min = None
        self._valley_filling_load_max = None
        self._voltage_level = None

    @property
    def construction(self):
        return self._construction

    @construction.setter
    def construction(self, value):
        self._construction = value
    @property
    def demand_load_max(self):
        return self._demand_load_max

    @demand_load_max.setter
    def demand_load_max(self, value):
        self._demand_load_max = value
    @property
    def electric_account(self):
        return self._electric_account

    @electric_account.setter
    def electric_account(self, value):
        self._electric_account = value
    @property
    def peak_shaving_load_max(self):
        return self._peak_shaving_load_max

    @peak_shaving_load_max.setter
    def peak_shaving_load_max(self, value):
        self._peak_shaving_load_max = value
    @property
    def service_tel(self):
        return self._service_tel

    @service_tel.setter
    def service_tel(self, value):
        self._service_tel = value
    @property
    def transformer_load_max(self):
        return self._transformer_load_max

    @transformer_load_max.setter
    def transformer_load_max(self, value):
        self._transformer_load_max = value
    @property
    def transformer_load_min(self):
        return self._transformer_load_min

    @transformer_load_min.setter
    def transformer_load_min(self, value):
        self._transformer_load_min = value
    @property
    def valley_filling_load_max(self):
        return self._valley_filling_load_max

    @valley_filling_load_max.setter
    def valley_filling_load_max(self, value):
        self._valley_filling_load_max = value
    @property
    def voltage_level(self):
        return self._voltage_level

    @voltage_level.setter
    def voltage_level(self, value):
        self._voltage_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.construction:
            if hasattr(self.construction, 'to_alipay_dict'):
                params['construction'] = self.construction.to_alipay_dict()
            else:
                params['construction'] = self.construction
        if self.demand_load_max:
            if hasattr(self.demand_load_max, 'to_alipay_dict'):
                params['demand_load_max'] = self.demand_load_max.to_alipay_dict()
            else:
                params['demand_load_max'] = self.demand_load_max
        if self.electric_account:
            if hasattr(self.electric_account, 'to_alipay_dict'):
                params['electric_account'] = self.electric_account.to_alipay_dict()
            else:
                params['electric_account'] = self.electric_account
        if self.peak_shaving_load_max:
            if hasattr(self.peak_shaving_load_max, 'to_alipay_dict'):
                params['peak_shaving_load_max'] = self.peak_shaving_load_max.to_alipay_dict()
            else:
                params['peak_shaving_load_max'] = self.peak_shaving_load_max
        if self.service_tel:
            if hasattr(self.service_tel, 'to_alipay_dict'):
                params['service_tel'] = self.service_tel.to_alipay_dict()
            else:
                params['service_tel'] = self.service_tel
        if self.transformer_load_max:
            if hasattr(self.transformer_load_max, 'to_alipay_dict'):
                params['transformer_load_max'] = self.transformer_load_max.to_alipay_dict()
            else:
                params['transformer_load_max'] = self.transformer_load_max
        if self.transformer_load_min:
            if hasattr(self.transformer_load_min, 'to_alipay_dict'):
                params['transformer_load_min'] = self.transformer_load_min.to_alipay_dict()
            else:
                params['transformer_load_min'] = self.transformer_load_min
        if self.valley_filling_load_max:
            if hasattr(self.valley_filling_load_max, 'to_alipay_dict'):
                params['valley_filling_load_max'] = self.valley_filling_load_max.to_alipay_dict()
            else:
                params['valley_filling_load_max'] = self.valley_filling_load_max
        if self.voltage_level:
            if hasattr(self.voltage_level, 'to_alipay_dict'):
                params['voltage_level'] = self.voltage_level.to_alipay_dict()
            else:
                params['voltage_level'] = self.voltage_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrustStationInfo()
        if 'construction' in d:
            o.construction = d['construction']
        if 'demand_load_max' in d:
            o.demand_load_max = d['demand_load_max']
        if 'electric_account' in d:
            o.electric_account = d['electric_account']
        if 'peak_shaving_load_max' in d:
            o.peak_shaving_load_max = d['peak_shaving_load_max']
        if 'service_tel' in d:
            o.service_tel = d['service_tel']
        if 'transformer_load_max' in d:
            o.transformer_load_max = d['transformer_load_max']
        if 'transformer_load_min' in d:
            o.transformer_load_min = d['transformer_load_min']
        if 'valley_filling_load_max' in d:
            o.valley_filling_load_max = d['valley_filling_load_max']
        if 'voltage_level' in d:
            o.voltage_level = d['voltage_level']
        return o


