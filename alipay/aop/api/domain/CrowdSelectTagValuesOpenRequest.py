#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdSelectTagValuesOpenRequest(object):

    def __init__(self):
        self._tag_id = None
        self._tag_option_category_id = None
        self._values = None

    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_option_category_id(self):
        return self._tag_option_category_id

    @tag_option_category_id.setter
    def tag_option_category_id(self, value):
        self._tag_option_category_id = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.tag_option_category_id:
            if hasattr(self.tag_option_category_id, 'to_alipay_dict'):
                params['tag_option_category_id'] = self.tag_option_category_id.to_alipay_dict()
            else:
                params['tag_option_category_id'] = self.tag_option_category_id
        if self.values:
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdSelectTagValuesOpenRequest()
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_option_category_id' in d:
            o.tag_option_category_id = d['tag_option_category_id']
        if 'values' in d:
            o.values = d['values']
        return o


