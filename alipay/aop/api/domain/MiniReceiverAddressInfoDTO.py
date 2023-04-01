#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniReceiverAddressInfoDTO(object):

    def __init__(self):
        self._detailed_address = None
        self._receiver_division_code = None
        self._receiver_name = None
        self._receiver_zip = None
        self._tel_number = None

    @property
    def detailed_address(self):
        return self._detailed_address

    @detailed_address.setter
    def detailed_address(self, value):
        self._detailed_address = value
    @property
    def receiver_division_code(self):
        return self._receiver_division_code

    @receiver_division_code.setter
    def receiver_division_code(self, value):
        self._receiver_division_code = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_zip(self):
        return self._receiver_zip

    @receiver_zip.setter
    def receiver_zip(self, value):
        self._receiver_zip = value
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
        if self.receiver_division_code:
            if hasattr(self.receiver_division_code, 'to_alipay_dict'):
                params['receiver_division_code'] = self.receiver_division_code.to_alipay_dict()
            else:
                params['receiver_division_code'] = self.receiver_division_code
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_zip:
            if hasattr(self.receiver_zip, 'to_alipay_dict'):
                params['receiver_zip'] = self.receiver_zip.to_alipay_dict()
            else:
                params['receiver_zip'] = self.receiver_zip
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
        o = MiniReceiverAddressInfoDTO()
        if 'detailed_address' in d:
            o.detailed_address = d['detailed_address']
        if 'receiver_division_code' in d:
            o.receiver_division_code = d['receiver_division_code']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_zip' in d:
            o.receiver_zip = d['receiver_zip']
        if 'tel_number' in d:
            o.tel_number = d['tel_number']
        return o


