#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantShopIndustryInfo(object):

    def __init__(self):
        self._info_code = None
        self._info_value = None

    @property
    def info_code(self):
        return self._info_code

    @info_code.setter
    def info_code(self, value):
        self._info_code = value
    @property
    def info_value(self):
        return self._info_value

    @info_value.setter
    def info_value(self, value):
        if isinstance(value, list):
            self._info_value = list()
            for i in value:
                self._info_value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.info_code:
            if hasattr(self.info_code, 'to_alipay_dict'):
                params['info_code'] = self.info_code.to_alipay_dict()
            else:
                params['info_code'] = self.info_code
        if self.info_value:
            if isinstance(self.info_value, list):
                for i in range(0, len(self.info_value)):
                    element = self.info_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.info_value[i] = element.to_alipay_dict()
            if hasattr(self.info_value, 'to_alipay_dict'):
                params['info_value'] = self.info_value.to_alipay_dict()
            else:
                params['info_value'] = self.info_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantShopIndustryInfo()
        if 'info_code' in d:
            o.info_code = d['info_code']
        if 'info_value' in d:
            o.info_value = d['info_value']
        return o


