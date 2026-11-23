#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceRefinedOilGasStationInfo(object):

    def __init__(self):
        self._gas_gun_no = None
        self._plate_no = None

    @property
    def gas_gun_no(self):
        return self._gas_gun_no

    @gas_gun_no.setter
    def gas_gun_no(self, value):
        self._gas_gun_no = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.gas_gun_no:
            if hasattr(self.gas_gun_no, 'to_alipay_dict'):
                params['gas_gun_no'] = self.gas_gun_no.to_alipay_dict()
            else:
                params['gas_gun_no'] = self.gas_gun_no
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceRefinedOilGasStationInfo()
        if 'gas_gun_no' in d:
            o.gas_gun_no = d['gas_gun_no']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        return o


