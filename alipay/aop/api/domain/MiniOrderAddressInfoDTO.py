#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniOrderAddressInfoDTO(object):

    def __init__(self):
        self._detailed_address = None
        self._division_code = None
        self._name = None
        self._tel_number = None

    @property
    def detailed_address(self):
        return self._detailed_address

    @detailed_address.setter
    def detailed_address(self, value):
        self._detailed_address = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tel_number(self):
        return self._tel_number

    @tel_number.setter
    def tel_number(self, value):
        self._tel_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.detailed_address:
            if hasattr(self.detailed_address, 'to_alipay_dict'):
                params['detailed_address'] = self.detailed_address.to_alipay_dict()
            else:
                params['detailed_address'] = self.detailed_address
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tel_number:
            if hasattr(self.tel_number, 'to_alipay_dict'):
                params['tel_number'] = self.tel_number.to_alipay_dict()
            else:
                params['tel_number'] = self.tel_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniOrderAddressInfoDTO()
        if 'detailed_address' in d:
            o.detailed_address = d['detailed_address']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'name' in d:
            o.name = d['name']
        if 'tel_number' in d:
            o.tel_number = d['tel_number']
        return o


