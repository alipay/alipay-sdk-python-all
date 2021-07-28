#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandResult import BrandResult


class MerchantBrandListResult(object):

    def __init__(self):
        self._brand_list_result = None

    @property
    def brand_list_result(self):
        return self._brand_list_result

    @brand_list_result.setter
    def brand_list_result(self, value):
        if isinstance(value, list):
            self._brand_list_result = list()
            for i in value:
                if isinstance(i, BrandResult):
                    self._brand_list_result.append(i)
                else:
                    self._brand_list_result.append(BrandResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.brand_list_result:
            if isinstance(self.brand_list_result, list):
                for i in range(0, len(self.brand_list_result)):
                    element = self.brand_list_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_list_result[i] = element.to_alipay_dict()
            if hasattr(self.brand_list_result, 'to_alipay_dict'):
                params['brand_list_result'] = self.brand_list_result.to_alipay_dict()
            else:
                params['brand_list_result'] = self.brand_list_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantBrandListResult()
        if 'brand_list_result' in d:
            o.brand_list_result = d['brand_list_result']
        return o


