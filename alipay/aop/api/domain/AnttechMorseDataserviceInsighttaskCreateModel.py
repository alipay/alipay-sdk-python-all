#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsightBrand import InsightBrand


class AnttechMorseDataserviceInsighttaskCreateModel(object):

    def __init__(self):
        self._brands = None
        self._consult_id = None
        self._type_info = None

    @property
    def brands(self):
        return self._brands

    @brands.setter
    def brands(self, value):
        if isinstance(value, list):
            self._brands = list()
            for i in value:
                if isinstance(i, InsightBrand):
                    self._brands.append(i)
                else:
                    self._brands.append(InsightBrand.from_alipay_dict(i))
    @property
    def consult_id(self):
        return self._consult_id

    @consult_id.setter
    def consult_id(self, value):
        self._consult_id = value
    @property
    def type_info(self):
        return self._type_info

    @type_info.setter
    def type_info(self, value):
        self._type_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.brands:
            if isinstance(self.brands, list):
                for i in range(0, len(self.brands)):
                    element = self.brands[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brands[i] = element.to_alipay_dict()
            if hasattr(self.brands, 'to_alipay_dict'):
                params['brands'] = self.brands.to_alipay_dict()
            else:
                params['brands'] = self.brands
        if self.consult_id:
            if hasattr(self.consult_id, 'to_alipay_dict'):
                params['consult_id'] = self.consult_id.to_alipay_dict()
            else:
                params['consult_id'] = self.consult_id
        if self.type_info:
            if hasattr(self.type_info, 'to_alipay_dict'):
                params['type_info'] = self.type_info.to_alipay_dict()
            else:
                params['type_info'] = self.type_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseDataserviceInsighttaskCreateModel()
        if 'brands' in d:
            o.brands = d['brands']
        if 'consult_id' in d:
            o.consult_id = d['consult_id']
        if 'type_info' in d:
            o.type_info = d['type_info']
        return o


