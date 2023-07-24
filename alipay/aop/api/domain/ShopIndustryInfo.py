#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopIndustryInfo(object):

    def __init__(self):
        self._first_industry = None
        self._second_industry = None
        self._third_industry = None

    @property
    def first_industry(self):
        return self._first_industry

    @first_industry.setter
    def first_industry(self, value):
        self._first_industry = value
    @property
    def second_industry(self):
        return self._second_industry

    @second_industry.setter
    def second_industry(self, value):
        self._second_industry = value
    @property
    def third_industry(self):
        return self._third_industry

    @third_industry.setter
    def third_industry(self, value):
        self._third_industry = value


    def to_alipay_dict(self):
        params = dict()
        if self.first_industry:
            if hasattr(self.first_industry, 'to_alipay_dict'):
                params['first_industry'] = self.first_industry.to_alipay_dict()
            else:
                params['first_industry'] = self.first_industry
        if self.second_industry:
            if hasattr(self.second_industry, 'to_alipay_dict'):
                params['second_industry'] = self.second_industry.to_alipay_dict()
            else:
                params['second_industry'] = self.second_industry
        if self.third_industry:
            if hasattr(self.third_industry, 'to_alipay_dict'):
                params['third_industry'] = self.third_industry.to_alipay_dict()
            else:
                params['third_industry'] = self.third_industry
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopIndustryInfo()
        if 'first_industry' in d:
            o.first_industry = d['first_industry']
        if 'second_industry' in d:
            o.second_industry = d['second_industry']
        if 'third_industry' in d:
            o.third_industry = d['third_industry']
        return o


