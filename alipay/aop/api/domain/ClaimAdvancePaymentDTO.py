#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimAdvancePaymentDTO(object):

    def __init__(self):
        self._claim_no = None
        self._claim_report_no = None
        self._in_account_name = None
        self._in_account_no = None
        self._in_account_type = None
        self._out_account_name = None
        self._out_account_no = None
        self._out_account_type = None
        self._pay_bill_no = None
        self._pay_channel = None
        self._pay_fee = None
        self._pay_order_no = None
        self._pay_out_biz_no = None
        self._pay_time = None
        self._policy_no = None

    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def in_account_name(self):
        return self._in_account_name

    @in_account_name.setter
    def in_account_name(self, value):
        self._in_account_name = value
    @property
    def in_account_no(self):
        return self._in_account_no

    @in_account_no.setter
    def in_account_no(self, value):
        self._in_account_no = value
    @property
    def in_account_type(self):
        return self._in_account_type

    @in_account_type.setter
    def in_account_type(self, value):
        self._in_account_type = value
    @property
    def out_account_name(self):
        return self._out_account_name

    @out_account_name.setter
    def out_account_name(self, value):
        self._out_account_name = value
    @property
    def out_account_no(self):
        return self._out_account_no

    @out_account_no.setter
    def out_account_no(self, value):
        self._out_account_no = value
    @property
    def out_account_type(self):
        return self._out_account_type

    @out_account_type.setter
    def out_account_type(self, value):
        self._out_account_type = value
    @property
    def pay_bill_no(self):
        return self._pay_bill_no

    @pay_bill_no.setter
    def pay_bill_no(self, value):
        self._pay_bill_no = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def pay_fee(self):
        return self._pay_fee

    @pay_fee.setter
    def pay_fee(self, value):
        self._pay_fee = value
    @property
    def pay_order_no(self):
        return self._pay_order_no

    @pay_order_no.setter
    def pay_order_no(self, value):
        self._pay_order_no = value
    @property
    def pay_out_biz_no(self):
        return self._pay_out_biz_no

    @pay_out_biz_no.setter
    def pay_out_biz_no(self, value):
        self._pay_out_biz_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.in_account_name:
            if hasattr(self.in_account_name, 'to_alipay_dict'):
                params['in_account_name'] = self.in_account_name.to_alipay_dict()
            else:
                params['in_account_name'] = self.in_account_name
        if self.in_account_no:
            if hasattr(self.in_account_no, 'to_alipay_dict'):
                params['in_account_no'] = self.in_account_no.to_alipay_dict()
            else:
                params['in_account_no'] = self.in_account_no
        if self.in_account_type:
            if hasattr(self.in_account_type, 'to_alipay_dict'):
                params['in_account_type'] = self.in_account_type.to_alipay_dict()
            else:
                params['in_account_type'] = self.in_account_type
        if self.out_account_name:
            if hasattr(self.out_account_name, 'to_alipay_dict'):
                params['out_account_name'] = self.out_account_name.to_alipay_dict()
            else:
                params['out_account_name'] = self.out_account_name
        if self.out_account_no:
            if hasattr(self.out_account_no, 'to_alipay_dict'):
                params['out_account_no'] = self.out_account_no.to_alipay_dict()
            else:
                params['out_account_no'] = self.out_account_no
        if self.out_account_type:
            if hasattr(self.out_account_type, 'to_alipay_dict'):
                params['out_account_type'] = self.out_account_type.to_alipay_dict()
            else:
                params['out_account_type'] = self.out_account_type
        if self.pay_bill_no:
            if hasattr(self.pay_bill_no, 'to_alipay_dict'):
                params['pay_bill_no'] = self.pay_bill_no.to_alipay_dict()
            else:
                params['pay_bill_no'] = self.pay_bill_no
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.pay_fee:
            if hasattr(self.pay_fee, 'to_alipay_dict'):
                params['pay_fee'] = self.pay_fee.to_alipay_dict()
            else:
                params['pay_fee'] = self.pay_fee
        if self.pay_order_no:
            if hasattr(self.pay_order_no, 'to_alipay_dict'):
                params['pay_order_no'] = self.pay_order_no.to_alipay_dict()
            else:
                params['pay_order_no'] = self.pay_order_no
        if self.pay_out_biz_no:
            if hasattr(self.pay_out_biz_no, 'to_alipay_dict'):
                params['pay_out_biz_no'] = self.pay_out_biz_no.to_alipay_dict()
            else:
                params['pay_out_biz_no'] = self.pay_out_biz_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimAdvancePaymentDTO()
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'in_account_name' in d:
            o.in_account_name = d['in_account_name']
        if 'in_account_no' in d:
            o.in_account_no = d['in_account_no']
        if 'in_account_type' in d:
            o.in_account_type = d['in_account_type']
        if 'out_account_name' in d:
            o.out_account_name = d['out_account_name']
        if 'out_account_no' in d:
            o.out_account_no = d['out_account_no']
        if 'out_account_type' in d:
            o.out_account_type = d['out_account_type']
        if 'pay_bill_no' in d:
            o.pay_bill_no = d['pay_bill_no']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'pay_fee' in d:
            o.pay_fee = d['pay_fee']
        if 'pay_order_no' in d:
            o.pay_order_no = d['pay_order_no']
        if 'pay_out_biz_no' in d:
            o.pay_out_biz_no = d['pay_out_biz_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        return o


