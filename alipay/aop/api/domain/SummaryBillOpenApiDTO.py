#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class SummaryBillOpenApiDTO(object):

    def __init__(self):
        self._adjust_amount = None
        self._bill_amount = None
        self._bill_month = None
        self._bill_no = None
        self._bill_status = None
        self._inst_id = None
        self._payee_ip_role_id = None
        self._real_bill_amount = None
        self._settle_ip_role_id = None
        self._settle_status = None
        self._settle_time_type = None
        self._settled_amount = None

    @property
    def adjust_amount(self):
        return self._adjust_amount

    @adjust_amount.setter
    def adjust_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._adjust_amount = value
        else:
            self._adjust_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_amount = value
        else:
            self._bill_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def bill_month(self):
        return self._bill_month

    @bill_month.setter
    def bill_month(self, value):
        self._bill_month = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def payee_ip_role_id(self):
        return self._payee_ip_role_id

    @payee_ip_role_id.setter
    def payee_ip_role_id(self, value):
        self._payee_ip_role_id = value
    @property
    def real_bill_amount(self):
        return self._real_bill_amount

    @real_bill_amount.setter
    def real_bill_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._real_bill_amount = value
        else:
            self._real_bill_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settle_time_type(self):
        return self._settle_time_type

    @settle_time_type.setter
    def settle_time_type(self, value):
        self._settle_time_type = value
    @property
    def settled_amount(self):
        return self._settled_amount

    @settled_amount.setter
    def settled_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settled_amount = value
        else:
            self._settled_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_amount:
            if hasattr(self.adjust_amount, 'to_alipay_dict'):
                params['adjust_amount'] = self.adjust_amount.to_alipay_dict()
            else:
                params['adjust_amount'] = self.adjust_amount
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_month:
            if hasattr(self.bill_month, 'to_alipay_dict'):
                params['bill_month'] = self.bill_month.to_alipay_dict()
            else:
                params['bill_month'] = self.bill_month
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.payee_ip_role_id:
            if hasattr(self.payee_ip_role_id, 'to_alipay_dict'):
                params['payee_ip_role_id'] = self.payee_ip_role_id.to_alipay_dict()
            else:
                params['payee_ip_role_id'] = self.payee_ip_role_id
        if self.real_bill_amount:
            if hasattr(self.real_bill_amount, 'to_alipay_dict'):
                params['real_bill_amount'] = self.real_bill_amount.to_alipay_dict()
            else:
                params['real_bill_amount'] = self.real_bill_amount
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settle_time_type:
            if hasattr(self.settle_time_type, 'to_alipay_dict'):
                params['settle_time_type'] = self.settle_time_type.to_alipay_dict()
            else:
                params['settle_time_type'] = self.settle_time_type
        if self.settled_amount:
            if hasattr(self.settled_amount, 'to_alipay_dict'):
                params['settled_amount'] = self.settled_amount.to_alipay_dict()
            else:
                params['settled_amount'] = self.settled_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SummaryBillOpenApiDTO()
        if 'adjust_amount' in d:
            o.adjust_amount = d['adjust_amount']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'payee_ip_role_id' in d:
            o.payee_ip_role_id = d['payee_ip_role_id']
        if 'real_bill_amount' in d:
            o.real_bill_amount = d['real_bill_amount']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_time_type' in d:
            o.settle_time_type = d['settle_time_type']
        if 'settled_amount' in d:
            o.settled_amount = d['settled_amount']
        return o


