#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiverAddressInfoDTO(object):

    def __init__(self):
        self._receiver_address = None
        self._receiver_division_code = None
        self._receiver_mobile = None
        self._receiver_name = None
        self._receiver_zip = None

    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_division_code(self):
        return self._receiver_division_code

    @receiver_division_code.setter
    def receiver_division_code(self, value):
        self._receiver_division_code = value
    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, value):
        self._receiver_mobile = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_division_code:
            if hasattr(self.receiver_division_code, 'to_alipay_dict'):
                params['receiver_division_code'] = self.receiver_division_code.to_alipay_dict()
            else:
                params['receiver_division_code'] = self.receiver_division_code
        if self.receiver_mobile:
            if hasattr(self.receiver_mobile, 'to_alipay_dict'):
                params['receiver_mobile'] = self.receiver_mobile.to_alipay_dict()
            else:
                params['receiver_mobile'] = self.receiver_mobile
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiverAddressInfoDTO()
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_division_code' in d:
            o.receiver_division_code = d['receiver_division_code']
        if 'receiver_mobile' in d:
            o.receiver_mobile = d['receiver_mobile']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_zip' in d:
            o.receiver_zip = d['receiver_zip']
        return o


