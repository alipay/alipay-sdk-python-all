#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ActivePayAndPrepayReverseCancelOpenApiOrder(object):

    def __init__(self):
        self._cancel_amount = None
        self._idempotent_no = None
        self._ip_role_source = None
        self._memo = None
        self._operator = None
        self._out_biz_no = None
        self._settle_ip_role_id = None
        self._source = None

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
    def ip_role_source(self):
        return self._ip_role_source

    @ip_role_source.setter
    def ip_role_source(self, value):
        self._ip_role_source = value
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
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


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
        if self.ip_role_source:
            if hasattr(self.ip_role_source, 'to_alipay_dict'):
                params['ip_role_source'] = self.ip_role_source.to_alipay_dict()
            else:
                params['ip_role_source'] = self.ip_role_source
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
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivePayAndPrepayReverseCancelOpenApiOrder()
        if 'cancel_amount' in d:
            o.cancel_amount = d['cancel_amount']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'ip_role_source' in d:
            o.ip_role_source = d['ip_role_source']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        if 'source' in d:
            o.source = d['source']
        return o


