#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductOption(object):

    def __init__(self):
        self._max_unit = None
        self._min_unit = None
        self._option_code = None
        self._sub_title = None
        self._title = None

    @property
    def max_unit(self):
        return self._max_unit

    @max_unit.setter
    def max_unit(self, value):
        self._max_unit = value
    @property
    def min_unit(self):
        return self._min_unit

    @min_unit.setter
    def min_unit(self, value):
        self._min_unit = value
    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_unit:
            if hasattr(self.max_unit, 'to_alipay_dict'):
                params['max_unit'] = self.max_unit.to_alipay_dict()
            else:
                params['max_unit'] = self.max_unit
        if self.min_unit:
            if hasattr(self.min_unit, 'to_alipay_dict'):
                params['min_unit'] = self.min_unit.to_alipay_dict()
            else:
                params['min_unit'] = self.min_unit
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductOption()
        if 'max_unit' in d:
            o.max_unit = d['max_unit']
        if 'min_unit' in d:
            o.min_unit = d['min_unit']
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


