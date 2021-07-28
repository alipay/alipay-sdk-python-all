#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.UserIdentityExt import UserIdentityExt


class AlipayBusinessPaymenthubRefundModel(object):

    def __init__(self):
        self._payee = None
        self._payee_ext = None
        self._payment_id = None
        self._refund_amount = None
        self._refund_request_no = None
        self._remark = None

    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        if isinstance(value, UserIdentity):
            self._payee = value
        else:
            self._payee = UserIdentity.from_alipay_dict(value)
    @property
    def payee_ext(self):
        return self._payee_ext

    @payee_ext.setter
    def payee_ext(self, value):
        if isinstance(value, UserIdentityExt):
            self._payee_ext = value
        else:
            self._payee_ext = UserIdentityExt.from_alipay_dict(value)
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.payee_ext:
            if hasattr(self.payee_ext, 'to_alipay_dict'):
                params['payee_ext'] = self.payee_ext.to_alipay_dict()
            else:
                params['payee_ext'] = self.payee_ext
        if self.payment_id:
            if hasattr(self.payment_id, 'to_alipay_dict'):
                params['payment_id'] = self.payment_id.to_alipay_dict()
            else:
                params['payment_id'] = self.payment_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_request_no:
            if hasattr(self.refund_request_no, 'to_alipay_dict'):
                params['refund_request_no'] = self.refund_request_no.to_alipay_dict()
            else:
                params['refund_request_no'] = self.refund_request_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessPaymenthubRefundModel()
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_ext' in d:
            o.payee_ext = d['payee_ext']
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_request_no' in d:
            o.refund_request_no = d['refund_request_no']
        if 'remark' in d:
            o.remark = d['remark']
        return o


