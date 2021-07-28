#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipassInstanceOpInfo(object):

    def __init__(self):
        self._order = None
        self._tpl_id = None
        self._tpl_params = None

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value
    @property
    def tpl_params(self):
        return self._tpl_params

    @tpl_params.setter
    def tpl_params(self, value):
        self._tpl_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        if self.tpl_params:
            if hasattr(self.tpl_params, 'to_alipay_dict'):
                params['tpl_params'] = self.tpl_params.to_alipay_dict()
            else:
                params['tpl_params'] = self.tpl_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipassInstanceOpInfo()
        if 'order' in d:
            o.order = d['order']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        if 'tpl_params' in d:
            o.tpl_params = d['tpl_params']
        return o


