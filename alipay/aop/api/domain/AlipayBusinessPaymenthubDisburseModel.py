#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.UserIdentityExt import UserIdentityExt


class AlipayBusinessPaymenthubDisburseModel(object):

    def __init__(self):
        self._disburse_amount = None
        self._disburse_request_no = None
        self._payee = None
        self._payee_ext = None
        self._payment_id = None
        self._remark = None

    @property
    def disburse_amount(self):
        return self._disburse_amount

    @disburse_amount.setter
    def disburse_amount(self, value):
        self._disburse_amount = value
    @property
    def disburse_request_no(self):
        return self._disburse_request_no

    @disburse_request_no.setter
    def disburse_request_no(self, value):
        self._disburse_request_no = value
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
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.disburse_amount:
            if hasattr(self.disburse_amount, 'to_alipay_dict'):
                params['disburse_amount'] = self.disburse_amount.to_alipay_dict()
            else:
                params['disburse_amount'] = self.disburse_amount
        if self.disburse_request_no:
            if hasattr(self.disburse_request_no, 'to_alipay_dict'):
                params['disburse_request_no'] = self.disburse_request_no.to_alipay_dict()
            else:
                params['disburse_request_no'] = self.disburse_request_no
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
        o = AlipayBusinessPaymenthubDisburseModel()
        if 'disburse_amount' in d:
            o.disburse_amount = d['disburse_amount']
        if 'disburse_request_no' in d:
            o.disburse_request_no = d['disburse_request_no']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_ext' in d:
            o.payee_ext = d['payee_ext']
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        if 'remark' in d:
            o.remark = d['remark']
        return o


