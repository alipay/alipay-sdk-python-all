#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddressInfoVO(object):

    def __init__(self):
        self._detailed_address = None
        self._receiver_name = None
        self._tel_number = None

    @property
    def detailed_address(self):
        return self._detailed_address

    @detailed_address.setter
    def detailed_address(self, value):
        self._detailed_address = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
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
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
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
        o = AddressInfoVO()
        if 'detailed_address' in d:
            o.detailed_address = d['detailed_address']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'tel_number' in d:
            o.tel_number = d['tel_number']
        return o


