#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentAbilityQueryResponse(object):

    def __init__(self):
        self._extra_infos = None
        self._level = None
        self._order_id = None

    @property
    def extra_infos(self):
        return self._extra_infos

    @extra_infos.setter
    def extra_infos(self, value):
        self._extra_infos = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_infos:
            if hasattr(self.extra_infos, 'to_alipay_dict'):
                params['extra_infos'] = self.extra_infos.to_alipay_dict()
            else:
                params['extra_infos'] = self.extra_infos
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentAbilityQueryResponse()
        if 'extra_infos' in d:
            o.extra_infos = d['extra_infos']
        if 'level' in d:
            o.level = d['level']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


