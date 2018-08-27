#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketMcommentQueryModel(object):

    def __init__(self):
        self._op_role = None
        self._partner_id = None
        self._trade_no = None

    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketMcommentQueryModel()
        if 'op_role' in d:
            o.op_role = d['op_role']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


