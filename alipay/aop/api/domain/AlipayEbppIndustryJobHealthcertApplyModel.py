#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobHealthcertApplyModel(object):

    def __init__(self):
        self._certify_return_url = None
        self._city_code = None
        self._fail_return_url = None
        self._jump_type = None

    @property
    def certify_return_url(self):
        return self._certify_return_url

    @certify_return_url.setter
    def certify_return_url(self, value):
        self._certify_return_url = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def fail_return_url(self):
        return self._fail_return_url

    @fail_return_url.setter
    def fail_return_url(self, value):
        self._fail_return_url = value
    @property
    def jump_type(self):
        return self._jump_type

    @jump_type.setter
    def jump_type(self, value):
        self._jump_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_return_url:
            if hasattr(self.certify_return_url, 'to_alipay_dict'):
                params['certify_return_url'] = self.certify_return_url.to_alipay_dict()
            else:
                params['certify_return_url'] = self.certify_return_url
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.fail_return_url:
            if hasattr(self.fail_return_url, 'to_alipay_dict'):
                params['fail_return_url'] = self.fail_return_url.to_alipay_dict()
            else:
                params['fail_return_url'] = self.fail_return_url
        if self.jump_type:
            if hasattr(self.jump_type, 'to_alipay_dict'):
                params['jump_type'] = self.jump_type.to_alipay_dict()
            else:
                params['jump_type'] = self.jump_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobHealthcertApplyModel()
        if 'certify_return_url' in d:
            o.certify_return_url = d['certify_return_url']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'fail_return_url' in d:
            o.fail_return_url = d['fail_return_url']
        if 'jump_type' in d:
            o.jump_type = d['jump_type']
        return o


