#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseAssetInfo(object):

    def __init__(self):
        self._asset_id = None
        self._asset_type = None
        self._employee_id = None
        self._employee_open_id = None
        self._pay_biz_type = None
        self._peer_pay_amount = None
        self._refund_id = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def employee_open_id(self):
        return self._employee_open_id

    @employee_open_id.setter
    def employee_open_id(self, value):
        self._employee_open_id = value
    @property
    def pay_biz_type(self):
        return self._pay_biz_type

    @pay_biz_type.setter
    def pay_biz_type(self, value):
        self._pay_biz_type = value
    @property
    def peer_pay_amount(self):
        return self._peer_pay_amount

    @peer_pay_amount.setter
    def peer_pay_amount(self, value):
        self._peer_pay_amount = value
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.employee_open_id:
            if hasattr(self.employee_open_id, 'to_alipay_dict'):
                params['employee_open_id'] = self.employee_open_id.to_alipay_dict()
            else:
                params['employee_open_id'] = self.employee_open_id
        if self.pay_biz_type:
            if hasattr(self.pay_biz_type, 'to_alipay_dict'):
                params['pay_biz_type'] = self.pay_biz_type.to_alipay_dict()
            else:
                params['pay_biz_type'] = self.pay_biz_type
        if self.peer_pay_amount:
            if hasattr(self.peer_pay_amount, 'to_alipay_dict'):
                params['peer_pay_amount'] = self.peer_pay_amount.to_alipay_dict()
            else:
                params['peer_pay_amount'] = self.peer_pay_amount
        if self.refund_id:
            if hasattr(self.refund_id, 'to_alipay_dict'):
                params['refund_id'] = self.refund_id.to_alipay_dict()
            else:
                params['refund_id'] = self.refund_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseAssetInfo()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'employee_open_id' in d:
            o.employee_open_id = d['employee_open_id']
        if 'pay_biz_type' in d:
            o.pay_biz_type = d['pay_biz_type']
        if 'peer_pay_amount' in d:
            o.peer_pay_amount = d['peer_pay_amount']
        if 'refund_id' in d:
            o.refund_id = d['refund_id']
        return o


