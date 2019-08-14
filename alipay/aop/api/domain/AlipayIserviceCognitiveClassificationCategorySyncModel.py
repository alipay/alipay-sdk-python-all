#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RubbishDTO import RubbishDTO


class AlipayIserviceCognitiveClassificationCategorySyncModel(object):

    def __init__(self):
        self._biz_code = None
        self._city_code = None
        self._rubbish_list = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def rubbish_list(self):
        return self._rubbish_list

    @rubbish_list.setter
    def rubbish_list(self, value):
        if isinstance(value, list):
            self._rubbish_list = list()
            for i in value:
                if isinstance(i, RubbishDTO):
                    self._rubbish_list.append(i)
                else:
                    self._rubbish_list.append(RubbishDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.rubbish_list:
            if isinstance(self.rubbish_list, list):
                for i in range(0, len(self.rubbish_list)):
                    element = self.rubbish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rubbish_list[i] = element.to_alipay_dict()
            if hasattr(self.rubbish_list, 'to_alipay_dict'):
                params['rubbish_list'] = self.rubbish_list.to_alipay_dict()
            else:
                params['rubbish_list'] = self.rubbish_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveClassificationCategorySyncModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'rubbish_list' in d:
            o.rubbish_list = d['rubbish_list']
        return o


