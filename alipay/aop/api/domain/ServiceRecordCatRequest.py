#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceRecordCatRequest(object):

    def __init__(self):
        self._cat_name = None
        self._first_cat = None
        self._fourth_cat = None
        self._instence_code = None
        self._second_cat = None
        self._third_cat = None

    @property
    def cat_name(self):
        return self._cat_name

    @cat_name.setter
    def cat_name(self, value):
        self._cat_name = value
    @property
    def first_cat(self):
        return self._first_cat

    @first_cat.setter
    def first_cat(self, value):
        self._first_cat = value
    @property
    def fourth_cat(self):
        return self._fourth_cat

    @fourth_cat.setter
    def fourth_cat(self, value):
        self._fourth_cat = value
    @property
    def instence_code(self):
        return self._instence_code

    @instence_code.setter
    def instence_code(self, value):
        self._instence_code = value
    @property
    def second_cat(self):
        return self._second_cat

    @second_cat.setter
    def second_cat(self, value):
        self._second_cat = value
    @property
    def third_cat(self):
        return self._third_cat

    @third_cat.setter
    def third_cat(self, value):
        self._third_cat = value


    def to_alipay_dict(self):
        params = dict()
        if self.cat_name:
            if hasattr(self.cat_name, 'to_alipay_dict'):
                params['cat_name'] = self.cat_name.to_alipay_dict()
            else:
                params['cat_name'] = self.cat_name
        if self.first_cat:
            if hasattr(self.first_cat, 'to_alipay_dict'):
                params['first_cat'] = self.first_cat.to_alipay_dict()
            else:
                params['first_cat'] = self.first_cat
        if self.fourth_cat:
            if hasattr(self.fourth_cat, 'to_alipay_dict'):
                params['fourth_cat'] = self.fourth_cat.to_alipay_dict()
            else:
                params['fourth_cat'] = self.fourth_cat
        if self.instence_code:
            if hasattr(self.instence_code, 'to_alipay_dict'):
                params['instence_code'] = self.instence_code.to_alipay_dict()
            else:
                params['instence_code'] = self.instence_code
        if self.second_cat:
            if hasattr(self.second_cat, 'to_alipay_dict'):
                params['second_cat'] = self.second_cat.to_alipay_dict()
            else:
                params['second_cat'] = self.second_cat
        if self.third_cat:
            if hasattr(self.third_cat, 'to_alipay_dict'):
                params['third_cat'] = self.third_cat.to_alipay_dict()
            else:
                params['third_cat'] = self.third_cat
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceRecordCatRequest()
        if 'cat_name' in d:
            o.cat_name = d['cat_name']
        if 'first_cat' in d:
            o.first_cat = d['first_cat']
        if 'fourth_cat' in d:
            o.fourth_cat = d['fourth_cat']
        if 'instence_code' in d:
            o.instence_code = d['instence_code']
        if 'second_cat' in d:
            o.second_cat = d['second_cat']
        if 'third_cat' in d:
            o.third_cat = d['third_cat']
        return o


