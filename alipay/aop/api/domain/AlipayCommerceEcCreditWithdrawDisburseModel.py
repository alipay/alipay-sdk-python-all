#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditWithdrawApplyInfo import CreditWithdrawApplyInfo


class AlipayCommerceEcCreditWithdrawDisburseModel(object):

    def __init__(self):
        self._credit_withdraw_apply_info_list = None
        self._enterprise_id = None
        self._trans_amount = None
        self._trans_serial_no = None
        self._trans_time = None

    @property
    def credit_withdraw_apply_info_list(self):
        return self._credit_withdraw_apply_info_list

    @credit_withdraw_apply_info_list.setter
    def credit_withdraw_apply_info_list(self, value):
        if isinstance(value, list):
            self._credit_withdraw_apply_info_list = list()
            for i in value:
                if isinstance(i, CreditWithdrawApplyInfo):
                    self._credit_withdraw_apply_info_list.append(i)
                else:
                    self._credit_withdraw_apply_info_list.append(CreditWithdrawApplyInfo.from_alipay_dict(i))
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_serial_no(self):
        return self._trans_serial_no

    @trans_serial_no.setter
    def trans_serial_no(self, value):
        self._trans_serial_no = value
    @property
    def trans_time(self):
        return self._trans_time

    @trans_time.setter
    def trans_time(self, value):
        self._trans_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_withdraw_apply_info_list:
            if isinstance(self.credit_withdraw_apply_info_list, list):
                for i in range(0, len(self.credit_withdraw_apply_info_list)):
                    element = self.credit_withdraw_apply_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_withdraw_apply_info_list[i] = element.to_alipay_dict()
            if hasattr(self.credit_withdraw_apply_info_list, 'to_alipay_dict'):
                params['credit_withdraw_apply_info_list'] = self.credit_withdraw_apply_info_list.to_alipay_dict()
            else:
                params['credit_withdraw_apply_info_list'] = self.credit_withdraw_apply_info_list
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_serial_no:
            if hasattr(self.trans_serial_no, 'to_alipay_dict'):
                params['trans_serial_no'] = self.trans_serial_no.to_alipay_dict()
            else:
                params['trans_serial_no'] = self.trans_serial_no
        if self.trans_time:
            if hasattr(self.trans_time, 'to_alipay_dict'):
                params['trans_time'] = self.trans_time.to_alipay_dict()
            else:
                params['trans_time'] = self.trans_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditWithdrawDisburseModel()
        if 'credit_withdraw_apply_info_list' in d:
            o.credit_withdraw_apply_info_list = d['credit_withdraw_apply_info_list']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_serial_no' in d:
            o.trans_serial_no = d['trans_serial_no']
        if 'trans_time' in d:
            o.trans_time = d['trans_time']
        return o


