#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiverAddressInfo(object):

    def __init__(self):
        self._address = None
        self._division_code = None
        self._mobile = None
        self._name = None
        self._zip = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.zip:
            if hasattr(self.zip, 'to_alipay_dict'):
                params['zip'] = self.zip.to_alipay_dict()
            else:
                params['zip'] = self.zip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiverAddressInfo()
        if 'address' in d:
            o.address = d['address']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'zip' in d:
            o.zip = d['zip']
        return o


