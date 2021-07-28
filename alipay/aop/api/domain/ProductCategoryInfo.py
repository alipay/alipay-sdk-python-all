#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductZoneInfo import ProductZoneInfo


class ProductCategoryInfo(object):

    def __init__(self):
        self._date = None
        self._desc = None
        self._name = None
        self._out_category_id = None
        self._zone_list = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_category_id(self):
        return self._out_category_id

    @out_category_id.setter
    def out_category_id(self, value):
        self._out_category_id = value
    @property
    def zone_list(self):
        return self._zone_list

    @zone_list.setter
    def zone_list(self, value):
        if isinstance(value, list):
            self._zone_list = list()
            for i in value:
                if isinstance(i, ProductZoneInfo):
                    self._zone_list.append(i)
                else:
                    self._zone_list.append(ProductZoneInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_category_id:
            if hasattr(self.out_category_id, 'to_alipay_dict'):
                params['out_category_id'] = self.out_category_id.to_alipay_dict()
            else:
                params['out_category_id'] = self.out_category_id
        if self.zone_list:
            if isinstance(self.zone_list, list):
                for i in range(0, len(self.zone_list)):
                    element = self.zone_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.zone_list[i] = element.to_alipay_dict()
            if hasattr(self.zone_list, 'to_alipay_dict'):
                params['zone_list'] = self.zone_list.to_alipay_dict()
            else:
                params['zone_list'] = self.zone_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductCategoryInfo()
        if 'date' in d:
            o.date = d['date']
        if 'desc' in d:
            o.desc = d['desc']
        if 'name' in d:
            o.name = d['name']
        if 'out_category_id' in d:
            o.out_category_id = d['out_category_id']
        if 'zone_list' in d:
            o.zone_list = d['zone_list']
        return o


