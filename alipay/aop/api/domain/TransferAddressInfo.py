#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferAddressInfo(object):

    def __init__(self):
        self._address_1 = None
        self._address_2 = None
        self._city = None
        self._region = None
        self._state = None
        self._zip_code = None

    @property
    def address_1(self):
        return self._address_1

    @address_1.setter
    def address_1(self, value):
        self._address_1 = value
    @property
    def address_2(self):
        return self._address_2

    @address_2.setter
    def address_2(self, value):
        self._address_2 = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_1:
            if hasattr(self.address_1, 'to_alipay_dict'):
                params['address_1'] = self.address_1.to_alipay_dict()
            else:
                params['address_1'] = self.address_1
        if self.address_2:
            if hasattr(self.address_2, 'to_alipay_dict'):
                params['address_2'] = self.address_2.to_alipay_dict()
            else:
                params['address_2'] = self.address_2
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.zip_code:
            if hasattr(self.zip_code, 'to_alipay_dict'):
                params['zip_code'] = self.zip_code.to_alipay_dict()
            else:
                params['zip_code'] = self.zip_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferAddressInfo()
        if 'address_1' in d:
            o.address_1 = d['address_1']
        if 'address_2' in d:
            o.address_2 = d['address_2']
        if 'city' in d:
            o.city = d['city']
        if 'region' in d:
            o.region = d['region']
        if 'state' in d:
            o.state = d['state']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o


