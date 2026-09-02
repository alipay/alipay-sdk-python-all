#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReferenceDataItem(object):

    def __init__(self):
        self._age_group = None
        self._gender = None
        self._reference_data = None
        self._value_type = None

    @property
    def age_group(self):
        return self._age_group

    @age_group.setter
    def age_group(self, value):
        self._age_group = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def reference_data(self):
        return self._reference_data

    @reference_data.setter
    def reference_data(self, value):
        self._reference_data = value
    @property
    def value_type(self):
        return self._value_type

    @value_type.setter
    def value_type(self, value):
        self._value_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_group:
            if hasattr(self.age_group, 'to_alipay_dict'):
                params['age_group'] = self.age_group.to_alipay_dict()
            else:
                params['age_group'] = self.age_group
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.reference_data:
            if hasattr(self.reference_data, 'to_alipay_dict'):
                params['reference_data'] = self.reference_data.to_alipay_dict()
            else:
                params['reference_data'] = self.reference_data
        if self.value_type:
            if hasattr(self.value_type, 'to_alipay_dict'):
                params['value_type'] = self.value_type.to_alipay_dict()
            else:
                params['value_type'] = self.value_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReferenceDataItem()
        if 'age_group' in d:
            o.age_group = d['age_group']
        if 'gender' in d:
            o.gender = d['gender']
        if 'reference_data' in d:
            o.reference_data = d['reference_data']
        if 'value_type' in d:
            o.value_type = d['value_type']
        return o


