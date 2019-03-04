#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtZftschoolQueryModel(object):

    def __init__(self):
        self._order_id = None
        self._partner_pid = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def partner_pid(self):
        return self._partner_pid

    @partner_pid.setter
    def partner_pid(self, value):
        self._partner_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.partner_pid:
            if hasattr(self.partner_pid, 'to_alipay_dict'):
                params['partner_pid'] = self.partner_pid.to_alipay_dict()
            else:
                params['partner_pid'] = self.partner_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtZftschoolQueryModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'partner_pid' in d:
            o.partner_pid = d['partner_pid']
        return o


