#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiValidStrategy(object):

    def __init__(self):
        self._gmt_invalid = None
        self._gmt_sign = None
        self._gmt_valid = None
        self._invalid_type = None
        self._valid_type = None

    @property
    def gmt_invalid(self):
        return self._gmt_invalid

    @gmt_invalid.setter
    def gmt_invalid(self, value):
        self._gmt_invalid = value
    @property
    def gmt_sign(self):
        return self._gmt_sign

    @gmt_sign.setter
    def gmt_sign(self, value):
        self._gmt_sign = value
    @property
    def gmt_valid(self):
        return self._gmt_valid

    @gmt_valid.setter
    def gmt_valid(self, value):
        self._gmt_valid = value
    @property
    def invalid_type(self):
        return self._invalid_type

    @invalid_type.setter
    def invalid_type(self, value):
        self._invalid_type = value
    @property
    def valid_type(self):
        return self._valid_type

    @valid_type.setter
    def valid_type(self, value):
        self._valid_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_invalid:
            if hasattr(self.gmt_invalid, 'to_alipay_dict'):
                params['gmt_invalid'] = self.gmt_invalid.to_alipay_dict()
            else:
                params['gmt_invalid'] = self.gmt_invalid
        if self.gmt_sign:
            if hasattr(self.gmt_sign, 'to_alipay_dict'):
                params['gmt_sign'] = self.gmt_sign.to_alipay_dict()
            else:
                params['gmt_sign'] = self.gmt_sign
        if self.gmt_valid:
            if hasattr(self.gmt_valid, 'to_alipay_dict'):
                params['gmt_valid'] = self.gmt_valid.to_alipay_dict()
            else:
                params['gmt_valid'] = self.gmt_valid
        if self.invalid_type:
            if hasattr(self.invalid_type, 'to_alipay_dict'):
                params['invalid_type'] = self.invalid_type.to_alipay_dict()
            else:
                params['invalid_type'] = self.invalid_type
        if self.valid_type:
            if hasattr(self.valid_type, 'to_alipay_dict'):
                params['valid_type'] = self.valid_type.to_alipay_dict()
            else:
                params['valid_type'] = self.valid_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiValidStrategy()
        if 'gmt_invalid' in d:
            o.gmt_invalid = d['gmt_invalid']
        if 'gmt_sign' in d:
            o.gmt_sign = d['gmt_sign']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        if 'invalid_type' in d:
            o.invalid_type = d['invalid_type']
        if 'valid_type' in d:
            o.valid_type = d['valid_type']
        return o


