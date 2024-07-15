#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RatePlanLabel(object):

    def __init__(self):
        self._label_category = None
        self._label_desc = None
        self._label_id = None
        self._label_name = None

    @property
    def label_category(self):
        return self._label_category

    @label_category.setter
    def label_category(self, value):
        self._label_category = value
    @property
    def label_desc(self):
        return self._label_desc

    @label_desc.setter
    def label_desc(self, value):
        self._label_desc = value
    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_category:
            if hasattr(self.label_category, 'to_alipay_dict'):
                params['label_category'] = self.label_category.to_alipay_dict()
            else:
                params['label_category'] = self.label_category
        if self.label_desc:
            if hasattr(self.label_desc, 'to_alipay_dict'):
                params['label_desc'] = self.label_desc.to_alipay_dict()
            else:
                params['label_desc'] = self.label_desc
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RatePlanLabel()
        if 'label_category' in d:
            o.label_category = d['label_category']
        if 'label_desc' in d:
            o.label_desc = d['label_desc']
        if 'label_id' in d:
            o.label_id = d['label_id']
        if 'label_name' in d:
            o.label_name = d['label_name']
        return o


