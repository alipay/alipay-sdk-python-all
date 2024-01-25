#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcpCityAreaItemList import IcpCityAreaItemList


class IcpProvinceAreaItemList(object):

    def __init__(self):
        self._city_area_items = None
        self._code = None
        self._name = None

    @property
    def city_area_items(self):
        return self._city_area_items

    @city_area_items.setter
    def city_area_items(self, value):
        if isinstance(value, list):
            self._city_area_items = list()
            for i in value:
                if isinstance(i, IcpCityAreaItemList):
                    self._city_area_items.append(i)
                else:
                    self._city_area_items.append(IcpCityAreaItemList.from_alipay_dict(i))
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_area_items:
            if isinstance(self.city_area_items, list):
                for i in range(0, len(self.city_area_items)):
                    element = self.city_area_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_area_items[i] = element.to_alipay_dict()
            if hasattr(self.city_area_items, 'to_alipay_dict'):
                params['city_area_items'] = self.city_area_items.to_alipay_dict()
            else:
                params['city_area_items'] = self.city_area_items
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcpProvinceAreaItemList()
        if 'city_area_items' in d:
            o.city_area_items = d['city_area_items']
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        return o


