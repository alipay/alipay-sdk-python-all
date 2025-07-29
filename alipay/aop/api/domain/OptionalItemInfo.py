#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OptionalItemInfo(object):

    def __init__(self):
        self._apply_count = None
        self._optional_item_id = None

    @property
    def apply_count(self):
        return self._apply_count

    @apply_count.setter
    def apply_count(self, value):
        self._apply_count = value
    @property
    def optional_item_id(self):
        return self._optional_item_id

    @optional_item_id.setter
    def optional_item_id(self, value):
        self._optional_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_count:
            if hasattr(self.apply_count, 'to_alipay_dict'):
                params['apply_count'] = self.apply_count.to_alipay_dict()
            else:
                params['apply_count'] = self.apply_count
        if self.optional_item_id:
            if hasattr(self.optional_item_id, 'to_alipay_dict'):
                params['optional_item_id'] = self.optional_item_id.to_alipay_dict()
            else:
                params['optional_item_id'] = self.optional_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OptionalItemInfo()
        if 'apply_count' in d:
            o.apply_count = d['apply_count']
        if 'optional_item_id' in d:
            o.optional_item_id = d['optional_item_id']
        return o


