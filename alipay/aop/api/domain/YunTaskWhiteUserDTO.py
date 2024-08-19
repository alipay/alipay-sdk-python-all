#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YunTaskWhiteUserDTO(object):

    def __init__(self):
        self._name = None
        self._white_phone = None
        self._white_type = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def white_phone(self):
        return self._white_phone

    @white_phone.setter
    def white_phone(self, value):
        self._white_phone = value
    @property
    def white_type(self):
        return self._white_type

    @white_type.setter
    def white_type(self, value):
        self._white_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.white_phone:
            if hasattr(self.white_phone, 'to_alipay_dict'):
                params['white_phone'] = self.white_phone.to_alipay_dict()
            else:
                params['white_phone'] = self.white_phone
        if self.white_type:
            if hasattr(self.white_type, 'to_alipay_dict'):
                params['white_type'] = self.white_type.to_alipay_dict()
            else:
                params['white_type'] = self.white_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskWhiteUserDTO()
        if 'name' in d:
            o.name = d['name']
        if 'white_phone' in d:
            o.white_phone = d['white_phone']
        if 'white_type' in d:
            o.white_type = d['white_type']
        return o


