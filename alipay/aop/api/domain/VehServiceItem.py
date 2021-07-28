#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehActivityItem import VehActivityItem


class VehServiceItem(object):

    def __init__(self):
        self._activity_items = None
        self._desc = None
        self._key = None

    @property
    def activity_items(self):
        return self._activity_items

    @activity_items.setter
    def activity_items(self, value):
        if isinstance(value, VehActivityItem):
            self._activity_items = value
        else:
            self._activity_items = VehActivityItem.from_alipay_dict(value)
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_items:
            if hasattr(self.activity_items, 'to_alipay_dict'):
                params['activity_items'] = self.activity_items.to_alipay_dict()
            else:
                params['activity_items'] = self.activity_items
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehServiceItem()
        if 'activity_items' in d:
            o.activity_items = d['activity_items']
        if 'desc' in d:
            o.desc = d['desc']
        if 'key' in d:
            o.key = d['key']
        return o


