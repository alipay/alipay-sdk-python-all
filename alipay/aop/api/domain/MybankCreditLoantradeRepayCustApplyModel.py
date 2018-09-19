#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MyBkAccountVO import MyBkAccountVO


class MybankCreditLoantradeRepayCustApplyModel(object):

    def __init__(self):
        self._apply_repay_fee = None
        self._apply_repay_int = None
        self._apply_repay_pre_fee = None
        self._apply_repay_prin = None
        self._discount_amt = None
        self._ext_data = None
        self._ip_id = None
        self._ip_role_id = None
        self._loan_ar_no = None
        self._prom_tools = None
        self._repay_account = None
        self._repay_type = None
        self._request_id = None

    @property
    def apply_repay_fee(self):
        return self._apply_repay_fee

    @apply_repay_fee.setter
    def apply_repay_fee(self, value):
        self._apply_repay_fee = value
    @property
    def apply_repay_int(self):
        return self._apply_repay_int

    @apply_repay_int.setter
    def apply_repay_int(self, value):
        self._apply_repay_int = value
    @property
    def apply_repay_pre_fee(self):
        return self._apply_repay_pre_fee

    @apply_repay_pre_fee.setter
    def apply_repay_pre_fee(self, value):
        self._apply_repay_pre_fee = value
    @property
    def apply_repay_prin(self):
        return self._apply_repay_prin

    @apply_repay_prin.setter
    def apply_repay_prin(self, value):
        self._apply_repay_prin = value
    @property
    def discount_amt(self):
        return self._discount_amt

    @discount_amt.setter
    def discount_amt(self, value):
        self._discount_amt = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def prom_tools(self):
        return self._prom_tools

    @prom_tools.setter
    def prom_tools(self, value):
        if isinstance(value, list):
            self._prom_tools = list()
            for i in value:
                self._prom_tools.append(i)
    @property
    def repay_account(self):
        return self._repay_account

    @repay_account.setter
    def repay_account(self, value):
        if isinstance(value, MyBkAccountVO):
            self._repay_account = value
        else:
            self._repay_account = MyBkAccountVO.from_alipay_dict(value)
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_repay_fee:
            if hasattr(self.apply_repay_fee, 'to_alipay_dict'):
                params['apply_repay_fee'] = self.apply_repay_fee.to_alipay_dict()
            else:
                params['apply_repay_fee'] = self.apply_repay_fee
        if self.apply_repay_int:
            if hasattr(self.apply_repay_int, 'to_alipay_dict'):
                params['apply_repay_int'] = self.apply_repay_int.to_alipay_dict()
            else:
                params['apply_repay_int'] = self.apply_repay_int
        if self.apply_repay_pre_fee:
            if hasattr(self.apply_repay_pre_fee, 'to_alipay_dict'):
                params['apply_repay_pre_fee'] = self.apply_repay_pre_fee.to_alipay_dict()
            else:
                params['apply_repay_pre_fee'] = self.apply_repay_pre_fee
        if self.apply_repay_prin:
            if hasattr(self.apply_repay_prin, 'to_alipay_dict'):
                params['apply_repay_prin'] = self.apply_repay_prin.to_alipay_dict()
            else:
                params['apply_repay_prin'] = self.apply_repay_prin
        if self.discount_amt:
            if hasattr(self.discount_amt, 'to_alipay_dict'):
                params['discount_amt'] = self.discount_amt.to_alipay_dict()
            else:
                params['discount_amt'] = self.discount_amt
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        if self.prom_tools:
            if isinstance(self.prom_tools, list):
                for i in range(0, len(self.prom_tools)):
                    element = self.prom_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prom_tools[i] = element.to_alipay_dict()
            if hasattr(self.prom_tools, 'to_alipay_dict'):
                params['prom_tools'] = self.prom_tools.to_alipay_dict()
            else:
                params['prom_tools'] = self.prom_tools
        if self.repay_account:
            if hasattr(self.repay_account, 'to_alipay_dict'):
                params['repay_account'] = self.repay_account.to_alipay_dict()
            else:
                params['repay_account'] = self.repay_account
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeRepayCustApplyModel()
        if 'apply_repay_fee' in d:
            o.apply_repay_fee = d['apply_repay_fee']
        if 'apply_repay_int' in d:
            o.apply_repay_int = d['apply_repay_int']
        if 'apply_repay_pre_fee' in d:
            o.apply_repay_pre_fee = d['apply_repay_pre_fee']
        if 'apply_repay_prin' in d:
            o.apply_repay_prin = d['apply_repay_prin']
        if 'discount_amt' in d:
            o.discount_amt = d['discount_amt']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        if 'prom_tools' in d:
            o.prom_tools = d['prom_tools']
        if 'repay_account' in d:
            o.repay_account = d['repay_account']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


