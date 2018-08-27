#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppCategoryInfo(object):

    def __init__(self):
        self._first_category_id = None
        self._first_category_name = None
        self._second_category_id = None
        self._second_category_name = None

    @property
    def first_category_id(self):
        return self._first_category_id

    @first_category_id.setter
    def first_category_id(self, value):
        self._first_category_id = value
    @property
    def first_category_name(self):
        return self._first_category_name

    @first_category_name.setter
    def first_category_name(self, value):
        self._first_category_name = value
    @property
    def second_category_id(self):
        return self._second_category_id

    @second_category_id.setter
    def second_category_id(self, value):
        self._second_category_id = value
    @property
    def second_category_name(self):
        return self._second_category_name

    @second_category_name.setter
    def second_category_name(self, value):
        self._second_category_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.first_category_id:
            if hasattr(self.first_category_id, 'to_alipay_dict'):
                params['first_category_id'] = self.first_category_id.to_alipay_dict()
            else:
                params['first_category_id'] = self.first_category_id
        if self.first_category_name:
            if hasattr(self.first_category_name, 'to_alipay_dict'):
                params['first_category_name'] = self.first_category_name.to_alipay_dict()
            else:
                params['first_category_name'] = self.first_category_name
        if self.second_category_id:
            if hasattr(self.second_category_id, 'to_alipay_dict'):
                params['second_category_id'] = self.second_category_id.to_alipay_dict()
            else:
                params['second_category_id'] = self.second_category_id
        if self.second_category_name:
            if hasattr(self.second_category_name, 'to_alipay_dict'):
                params['second_category_name'] = self.second_category_name.to_alipay_dict()
            else:
                params['second_category_name'] = self.second_category_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppCategoryInfo()
        if 'first_category_id' in d:
            o.first_category_id = d['first_category_id']
        if 'first_category_name' in d:
            o.first_category_name = d['first_category_name']
        if 'second_category_id' in d:
            o.second_category_id = d['second_category_id']
        if 'second_category_name' in d:
            o.second_category_name = d['second_category_name']
        return o


