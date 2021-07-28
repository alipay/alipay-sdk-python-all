#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity


class HuanxuTradeOrderRefundModel(object):

    def __init__(self):
        self._identity = None
        self._issuer = None
        self._payee = None
        self._payment_id = None
        self._refund_amount = None
        self._refund_request_no = None
        self._remark = None
        self._type = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def issuer(self):
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        self._issuer = value
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
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.issuer:
            if hasattr(self.issuer, 'to_alipay_dict'):
                params['issuer'] = self.issuer.to_alipay_dict()
            else:
                params['issuer'] = self.issuer
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HuanxuTradeOrderRefundModel()
        if 'identity' in d:
            o.identity = d['identity']
        if 'issuer' in d:
            o.issuer = d['issuer']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_request_no' in d:
            o.refund_request_no = d['refund_request_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'type' in d:
            o.type = d['type']
        return o


