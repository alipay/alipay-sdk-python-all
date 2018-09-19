#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MyObjectDdd(object):

    def __init__(self):
        self._item = None
        self._param = None

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        self._item = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value


    def to_alipay_dict(self):
        params = dict()
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MyObjectDdd()
        if 'item' in d:
            o.item = d['item']
        if 'param' in d:
            o.param = d['param']
        return o


