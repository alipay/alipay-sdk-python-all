#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbadvertChannelTypeResponse(object):

    def __init__(self):
        self._desc = None
        self._order = None
        self._type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbadvertChannelTypeResponse()
        if 'desc' in d:
            o.desc = d['desc']
        if 'order' in d:
            o.order = d['order']
        if 'type' in d:
            o.type = d['type']
        return o


