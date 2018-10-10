#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlateInfoForYiCai(object):

    def __init__(self):
        self._category = None
        self._id = None
        self._plate_name = None
        self._symbol_name = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def plate_name(self):
        return self._plate_name

    @plate_name.setter
    def plate_name(self, value):
        self._plate_name = value
    @property
    def symbol_name(self):
        return self._symbol_name

    @symbol_name.setter
    def symbol_name(self, value):
        if isinstance(value, list):
            self._symbol_name = list()
            for i in value:
                self._symbol_name.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.plate_name:
            if hasattr(self.plate_name, 'to_alipay_dict'):
                params['plate_name'] = self.plate_name.to_alipay_dict()
            else:
                params['plate_name'] = self.plate_name
        if self.symbol_name:
            if isinstance(self.symbol_name, list):
                for i in range(0, len(self.symbol_name)):
                    element = self.symbol_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbol_name[i] = element.to_alipay_dict()
            if hasattr(self.symbol_name, 'to_alipay_dict'):
                params['symbol_name'] = self.symbol_name.to_alipay_dict()
            else:
                params['symbol_name'] = self.symbol_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlateInfoForYiCai()
        if 'category' in d:
            o.category = d['category']
        if 'id' in d:
            o.id = d['id']
        if 'plate_name' in d:
            o.plate_name = d['plate_name']
        if 'symbol_name' in d:
            o.symbol_name = d['symbol_name']
        return o


