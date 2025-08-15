#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayInstructCloudTriggerModel(object):

    def __init__(self):
        self._amount = None
        self._bpaas_ipc_timeout = None
        self._cashier_type = None
        self._operate_type = None
        self._page = None
        self._pos_id = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bpaas_ipc_timeout(self):
        return self._bpaas_ipc_timeout

    @bpaas_ipc_timeout.setter
    def bpaas_ipc_timeout(self, value):
        self._bpaas_ipc_timeout = value
    @property
    def cashier_type(self):
        return self._cashier_type

    @cashier_type.setter
    def cashier_type(self, value):
        self._cashier_type = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def pos_id(self):
        return self._pos_id

    @pos_id.setter
    def pos_id(self, value):
        self._pos_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bpaas_ipc_timeout:
            if hasattr(self.bpaas_ipc_timeout, 'to_alipay_dict'):
                params['bpaas_ipc_timeout'] = self.bpaas_ipc_timeout.to_alipay_dict()
            else:
                params['bpaas_ipc_timeout'] = self.bpaas_ipc_timeout
        if self.cashier_type:
            if hasattr(self.cashier_type, 'to_alipay_dict'):
                params['cashier_type'] = self.cashier_type.to_alipay_dict()
            else:
                params['cashier_type'] = self.cashier_type
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.pos_id:
            if hasattr(self.pos_id, 'to_alipay_dict'):
                params['pos_id'] = self.pos_id.to_alipay_dict()
            else:
                params['pos_id'] = self.pos_id
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
        o = AlipayPayInstructCloudTriggerModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bpaas_ipc_timeout' in d:
            o.bpaas_ipc_timeout = d['bpaas_ipc_timeout']
        if 'cashier_type' in d:
            o.cashier_type = d['cashier_type']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'page' in d:
            o.page = d['page']
        if 'pos_id' in d:
            o.pos_id = d['pos_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


