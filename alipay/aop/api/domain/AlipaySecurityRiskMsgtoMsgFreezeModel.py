#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyouTestFour import JinyouTestFour


class AlipaySecurityRiskMsgtoMsgFreezeModel(object):

    def __init__(self):
        self._c_ka = None
        self._cert_no = None
        self._city_code = None
        self._license_expiry_date = None
        self._x_dd = None
        self._x_open_id = None

    @property
    def c_ka(self):
        return self._c_ka

    @c_ka.setter
    def c_ka(self, value):
        self._c_ka = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        if isinstance(value, list):
            self._cert_no = list()
            for i in value:
                self._cert_no.append(i)
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        if isinstance(value, JinyouTestFour):
            self._city_code = value
        else:
            self._city_code = JinyouTestFour.from_alipay_dict(value)
    @property
    def license_expiry_date(self):
        return self._license_expiry_date

    @license_expiry_date.setter
    def license_expiry_date(self, value):
        self._license_expiry_date = value
    @property
    def x_dd(self):
        return self._x_dd

    @x_dd.setter
    def x_dd(self, value):
        self._x_dd = value
    @property
    def x_open_id(self):
        return self._x_open_id

    @x_open_id.setter
    def x_open_id(self, value):
        self._x_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.c_ka:
            if hasattr(self.c_ka, 'to_alipay_dict'):
                params['c_ka'] = self.c_ka.to_alipay_dict()
            else:
                params['c_ka'] = self.c_ka
        if self.cert_no:
            if isinstance(self.cert_no, list):
                for i in range(0, len(self.cert_no)):
                    element = self.cert_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cert_no[i] = element.to_alipay_dict()
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.license_expiry_date:
            if hasattr(self.license_expiry_date, 'to_alipay_dict'):
                params['license_expiry_date'] = self.license_expiry_date.to_alipay_dict()
            else:
                params['license_expiry_date'] = self.license_expiry_date
        if self.x_dd:
            if hasattr(self.x_dd, 'to_alipay_dict'):
                params['x_dd'] = self.x_dd.to_alipay_dict()
            else:
                params['x_dd'] = self.x_dd
        if self.x_open_id:
            if hasattr(self.x_open_id, 'to_alipay_dict'):
                params['x_open_id'] = self.x_open_id.to_alipay_dict()
            else:
                params['x_open_id'] = self.x_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskMsgtoMsgFreezeModel()
        if 'c_ka' in d:
            o.c_ka = d['c_ka']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'license_expiry_date' in d:
            o.license_expiry_date = d['license_expiry_date']
        if 'x_dd' in d:
            o.x_dd = d['x_dd']
        if 'x_open_id' in d:
            o.x_open_id = d['x_open_id']
        return o


