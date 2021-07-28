#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationAddress(object):

    def __init__(self):
        self._address = None
        self._city = None
        self._region = None
        self._state = None
        self._zip_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
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
        o = OperationAddress()
        if 'address' in d:
            o.address = d['address']
        if 'city' in d:
            o.city = d['city']
        if 'region' in d:
            o.region = d['region']
        if 'state' in d:
            o.state = d['state']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o


