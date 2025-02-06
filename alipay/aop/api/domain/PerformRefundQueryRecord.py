#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PerformRefundQueryRecord(object):

    def __init__(self):
        self._amount = None
        self._bill_no = None
        self._gmt_refund_pay = None
        self._pay_no = None
        self._real_amount = None
        self._reason = None
        self._refund_charge_fee = None
        self._refund_error_info = None
        self._request_id = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def refund_charge_fee(self):
        return self._refund_charge_fee

    @refund_charge_fee.setter
    def refund_charge_fee(self, value):
        self._refund_charge_fee = value
    @property
    def refund_error_info(self):
        return self._refund_error_info

    @refund_error_info.setter
    def refund_error_info(self, value):
        self._refund_error_info = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.gmt_refund_pay:
            if hasattr(self.gmt_refund_pay, 'to_alipay_dict'):
                params['gmt_refund_pay'] = self.gmt_refund_pay.to_alipay_dict()
            else:
                params['gmt_refund_pay'] = self.gmt_refund_pay
        if self.pay_no:
            if hasattr(self.pay_no, 'to_alipay_dict'):
                params['pay_no'] = self.pay_no.to_alipay_dict()
            else:
                params['pay_no'] = self.pay_no
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.refund_charge_fee:
            if hasattr(self.refund_charge_fee, 'to_alipay_dict'):
                params['refund_charge_fee'] = self.refund_charge_fee.to_alipay_dict()
            else:
                params['refund_charge_fee'] = self.refund_charge_fee
        if self.refund_error_info:
            if hasattr(self.refund_error_info, 'to_alipay_dict'):
                params['refund_error_info'] = self.refund_error_info.to_alipay_dict()
            else:
                params['refund_error_info'] = self.refund_error_info
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = PerformRefundQueryRecord()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'gmt_refund_pay' in d:
            o.gmt_refund_pay = d['gmt_refund_pay']
        if 'pay_no' in d:
            o.pay_no = d['pay_no']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'reason' in d:
            o.reason = d['reason']
        if 'refund_charge_fee' in d:
            o.refund_charge_fee = d['refund_charge_fee']
        if 'refund_error_info' in d:
            o.refund_error_info = d['refund_error_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'status' in d:
            o.status = d['status']
        return o


