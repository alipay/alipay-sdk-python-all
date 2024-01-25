#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Facility(object):

    def __init__(self):
        self._category = None
        self._category_name = None
        self._facility_name = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def facility_name(self):
        return self._facility_name

    @facility_name.setter
    def facility_name(self, value):
        self._facility_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.facility_name:
            if hasattr(self.facility_name, 'to_alipay_dict'):
                params['facility_name'] = self.facility_name.to_alipay_dict()
            else:
                params['facility_name'] = self.facility_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Facility()
        if 'category' in d:
            o.category = d['category']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'facility_name' in d:
            o.facility_name = d['facility_name']
        return o


