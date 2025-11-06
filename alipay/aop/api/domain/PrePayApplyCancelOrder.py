#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class PrePayApplyCancelOrder(object):

    def __init__(self):
        self._cancel_amount = None
        self._idempotent_no = None
        self._ip_role_id = None
        self._memo = None
        self._operator = None
        self._out_biz_no = None

    @property
    def cancel_amount(self):
        return self._cancel_amount

    @cancel_amount.setter
    def cancel_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._cancel_amount = value
        else:
            self._cancel_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def idempotent_no(self):
        return self._idempotent_no

    @idempotent_no.setter
    def idempotent_no(self, value):
        self._idempotent_no = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_amount:
            if hasattr(self.cancel_amount, 'to_alipay_dict'):
                params['cancel_amount'] = self.cancel_amount.to_alipay_dict()
            else:
                params['cancel_amount'] = self.cancel_amount
        if self.idempotent_no:
            if hasattr(self.idempotent_no, 'to_alipay_dict'):
                params['idempotent_no'] = self.idempotent_no.to_alipay_dict()
            else:
                params['idempotent_no'] = self.idempotent_no
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrePayApplyCancelOrder()
        if 'cancel_amount' in d:
            o.cancel_amount = d['cancel_amount']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


