#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpensecomsueOutsourceNotifyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._amount = None
        self._deal_time = None
        self._employee_id = None
        self._employee_id_type = None
        self._extend = None
        self._is_off_set = None
        self._out_source_id = None
        self._platform = None
        self._relate_no = None
        self._standard_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def deal_time(self):
        return self._deal_time

    @deal_time.setter
    def deal_time(self, value):
        self._deal_time = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def employee_id_type(self):
        return self._employee_id_type

    @employee_id_type.setter
    def employee_id_type(self, value):
        self._employee_id_type = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def is_off_set(self):
        return self._is_off_set

    @is_off_set.setter
    def is_off_set(self, value):
        self._is_off_set = value
    @property
    def out_source_id(self):
        return self._out_source_id

    @out_source_id.setter
    def out_source_id(self, value):
        self._out_source_id = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def relate_no(self):
        return self._relate_no

    @relate_no.setter
    def relate_no(self, value):
        self._relate_no = value
    @property
    def standard_id(self):
        return self._standard_id

    @standard_id.setter
    def standard_id(self, value):
        self._standard_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.deal_time:
            if hasattr(self.deal_time, 'to_alipay_dict'):
                params['deal_time'] = self.deal_time.to_alipay_dict()
            else:
                params['deal_time'] = self.deal_time
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.employee_id_type:
            if hasattr(self.employee_id_type, 'to_alipay_dict'):
                params['employee_id_type'] = self.employee_id_type.to_alipay_dict()
            else:
                params['employee_id_type'] = self.employee_id_type
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.is_off_set:
            if hasattr(self.is_off_set, 'to_alipay_dict'):
                params['is_off_set'] = self.is_off_set.to_alipay_dict()
            else:
                params['is_off_set'] = self.is_off_set
        if self.out_source_id:
            if hasattr(self.out_source_id, 'to_alipay_dict'):
                params['out_source_id'] = self.out_source_id.to_alipay_dict()
            else:
                params['out_source_id'] = self.out_source_id
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.relate_no:
            if hasattr(self.relate_no, 'to_alipay_dict'):
                params['relate_no'] = self.relate_no.to_alipay_dict()
            else:
                params['relate_no'] = self.relate_no
        if self.standard_id:
            if hasattr(self.standard_id, 'to_alipay_dict'):
                params['standard_id'] = self.standard_id.to_alipay_dict()
            else:
                params['standard_id'] = self.standard_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpensecomsueOutsourceNotifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'deal_time' in d:
            o.deal_time = d['deal_time']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'employee_id_type' in d:
            o.employee_id_type = d['employee_id_type']
        if 'extend' in d:
            o.extend = d['extend']
        if 'is_off_set' in d:
            o.is_off_set = d['is_off_set']
        if 'out_source_id' in d:
            o.out_source_id = d['out_source_id']
        if 'platform' in d:
            o.platform = d['platform']
        if 'relate_no' in d:
            o.relate_no = d['relate_no']
        if 'standard_id' in d:
            o.standard_id = d['standard_id']
        return o


