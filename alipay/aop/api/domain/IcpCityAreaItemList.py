#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcpDistrictAreaItemList import IcpDistrictAreaItemList


class IcpCityAreaItemList(object):

    def __init__(self):
        self._code = None
        self._district_area_items = None
        self._name = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def district_area_items(self):
        return self._district_area_items

    @district_area_items.setter
    def district_area_items(self, value):
        if isinstance(value, list):
            self._district_area_items = list()
            for i in value:
                if isinstance(i, IcpDistrictAreaItemList):
                    self._district_area_items.append(i)
                else:
                    self._district_area_items.append(IcpDistrictAreaItemList.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.district_area_items:
            if isinstance(self.district_area_items, list):
                for i in range(0, len(self.district_area_items)):
                    element = self.district_area_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_area_items[i] = element.to_alipay_dict()
            if hasattr(self.district_area_items, 'to_alipay_dict'):
                params['district_area_items'] = self.district_area_items.to_alipay_dict()
            else:
                params['district_area_items'] = self.district_area_items
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
        o = IcpCityAreaItemList()
        if 'code' in d:
            o.code = d['code']
        if 'district_area_items' in d:
            o.district_area_items = d['district_area_items']
        if 'name' in d:
            o.name = d['name']
        return o


