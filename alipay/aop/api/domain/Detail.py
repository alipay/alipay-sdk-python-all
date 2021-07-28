#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Detail(object):

    def __init__(self):
        self._code = None
        self._description = None
        self._order = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Detail()
        if 'code' in d:
            o.code = d['code']
        if 'description' in d:
            o.description = d['description']
        if 'order' in d:
            o.order = d['order']
        return o


