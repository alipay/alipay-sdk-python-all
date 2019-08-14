#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInstcardBindModel(object):

    def __init__(self):
        self._city_code = None
        self._extend_params = None
        self._ins_code = None
        self._return_url = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def ins_code(self):
        return self._ins_code

    @ins_code.setter
    def ins_code(self, value):
        self._ins_code = value
    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.ins_code:
            if hasattr(self.ins_code, 'to_alipay_dict'):
                params['ins_code'] = self.ins_code.to_alipay_dict()
            else:
                params['ins_code'] = self.ins_code
        if self.return_url:
            if hasattr(self.return_url, 'to_alipay_dict'):
                params['return_url'] = self.return_url.to_alipay_dict()
            else:
                params['return_url'] = self.return_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInstcardBindModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'ins_code' in d:
            o.ins_code = d['ins_code']
        if 'return_url' in d:
            o.return_url = d['return_url']
        return o


