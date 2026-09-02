#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AucCredit import AucCredit
from alipay.aop.api.domain.AucLoanInfo import AucLoanInfo


class XingheLendassistCarfinauctionApplystatusNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._credit_list = None
        self._loan_info = None
        self._out_apply_no = None
        self._refuse_code = None
        self._refuse_msg = None
        self._status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def credit_list(self):
        return self._credit_list

    @credit_list.setter
    def credit_list(self, value):
        if isinstance(value, list):
            self._credit_list = list()
            for i in value:
                if isinstance(i, AucCredit):
                    self._credit_list.append(i)
                else:
                    self._credit_list.append(AucCredit.from_alipay_dict(i))
    @property
    def loan_info(self):
        return self._loan_info

    @loan_info.setter
    def loan_info(self, value):
        if isinstance(value, AucLoanInfo):
            self._loan_info = value
        else:
            self._loan_info = AucLoanInfo.from_alipay_dict(value)
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.credit_list:
            if isinstance(self.credit_list, list):
                for i in range(0, len(self.credit_list)):
                    element = self.credit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_list[i] = element.to_alipay_dict()
            if hasattr(self.credit_list, 'to_alipay_dict'):
                params['credit_list'] = self.credit_list.to_alipay_dict()
            else:
                params['credit_list'] = self.credit_list
        if self.loan_info:
            if hasattr(self.loan_info, 'to_alipay_dict'):
                params['loan_info'] = self.loan_info.to_alipay_dict()
            else:
                params['loan_info'] = self.loan_info
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinauctionApplystatusNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'credit_list' in d:
            o.credit_list = d['credit_list']
        if 'loan_info' in d:
            o.loan_info = d['loan_info']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'status' in d:
            o.status = d['status']
        return o


