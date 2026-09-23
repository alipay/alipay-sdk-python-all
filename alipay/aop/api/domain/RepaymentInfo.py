#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymentInfo(object):

    def __init__(self):
        self._amount = None
        self._fail_reason = None
        self._gmt_pay = None
        self._out_request_no = None
        self._payee_wallet_id = None
        self._payer_wallet_id = None
        self._repayment_status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def payee_wallet_id(self):
        return self._payee_wallet_id

    @payee_wallet_id.setter
    def payee_wallet_id(self, value):
        self._payee_wallet_id = value
    @property
    def payer_wallet_id(self):
        return self._payer_wallet_id

    @payer_wallet_id.setter
    def payer_wallet_id(self, value):
        self._payer_wallet_id = value
    @property
    def repayment_status(self):
        return self._repayment_status

    @repayment_status.setter
    def repayment_status(self, value):
        self._repayment_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.payee_wallet_id:
            if hasattr(self.payee_wallet_id, 'to_alipay_dict'):
                params['payee_wallet_id'] = self.payee_wallet_id.to_alipay_dict()
            else:
                params['payee_wallet_id'] = self.payee_wallet_id
        if self.payer_wallet_id:
            if hasattr(self.payer_wallet_id, 'to_alipay_dict'):
                params['payer_wallet_id'] = self.payer_wallet_id.to_alipay_dict()
            else:
                params['payer_wallet_id'] = self.payer_wallet_id
        if self.repayment_status:
            if hasattr(self.repayment_status, 'to_alipay_dict'):
                params['repayment_status'] = self.repayment_status.to_alipay_dict()
            else:
                params['repayment_status'] = self.repayment_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepaymentInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'payee_wallet_id' in d:
            o.payee_wallet_id = d['payee_wallet_id']
        if 'payer_wallet_id' in d:
            o.payer_wallet_id = d['payer_wallet_id']
        if 'repayment_status' in d:
            o.repayment_status = d['repayment_status']
        return o


