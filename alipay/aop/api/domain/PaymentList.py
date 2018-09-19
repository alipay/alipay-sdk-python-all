#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountInfos import DiscountInfos


class PaymentList(object):

    def __init__(self):
        self._amount = None
        self._discount_amount = None
        self._discount_infos = None
        self._ext_infos = None
        self._online_payment_no = None
        self._out_payment_id = None
        self._payment_id = None
        self._payment_method = None
        self._user_identity = None
        self._user_identity_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_infos(self):
        return self._discount_infos

    @discount_infos.setter
    def discount_infos(self, value):
        if isinstance(value, list):
            self._discount_infos = list()
            for i in value:
                if isinstance(i, DiscountInfos):
                    self._discount_infos.append(i)
                else:
                    self._discount_infos.append(DiscountInfos.from_alipay_dict(i))
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def online_payment_no(self):
        return self._online_payment_no

    @online_payment_no.setter
    def online_payment_no(self, value):
        self._online_payment_no = value
    @property
    def out_payment_id(self):
        return self._out_payment_id

    @out_payment_id.setter
    def out_payment_id(self, value):
        self._out_payment_id = value
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def user_identity(self):
        return self._user_identity

    @user_identity.setter
    def user_identity(self, value):
        self._user_identity = value
    @property
    def user_identity_type(self):
        return self._user_identity_type

    @user_identity_type.setter
    def user_identity_type(self, value):
        self._user_identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_infos:
            if isinstance(self.discount_infos, list):
                for i in range(0, len(self.discount_infos)):
                    element = self.discount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_infos[i] = element.to_alipay_dict()
            if hasattr(self.discount_infos, 'to_alipay_dict'):
                params['discount_infos'] = self.discount_infos.to_alipay_dict()
            else:
                params['discount_infos'] = self.discount_infos
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.online_payment_no:
            if hasattr(self.online_payment_no, 'to_alipay_dict'):
                params['online_payment_no'] = self.online_payment_no.to_alipay_dict()
            else:
                params['online_payment_no'] = self.online_payment_no
        if self.out_payment_id:
            if hasattr(self.out_payment_id, 'to_alipay_dict'):
                params['out_payment_id'] = self.out_payment_id.to_alipay_dict()
            else:
                params['out_payment_id'] = self.out_payment_id
        if self.payment_id:
            if hasattr(self.payment_id, 'to_alipay_dict'):
                params['payment_id'] = self.payment_id.to_alipay_dict()
            else:
                params['payment_id'] = self.payment_id
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.user_identity:
            if hasattr(self.user_identity, 'to_alipay_dict'):
                params['user_identity'] = self.user_identity.to_alipay_dict()
            else:
                params['user_identity'] = self.user_identity
        if self.user_identity_type:
            if hasattr(self.user_identity_type, 'to_alipay_dict'):
                params['user_identity_type'] = self.user_identity_type.to_alipay_dict()
            else:
                params['user_identity_type'] = self.user_identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentList()
        if 'amount' in d:
            o.amount = d['amount']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_infos' in d:
            o.discount_infos = d['discount_infos']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'online_payment_no' in d:
            o.online_payment_no = d['online_payment_no']
        if 'out_payment_id' in d:
            o.out_payment_id = d['out_payment_id']
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'user_identity' in d:
            o.user_identity = d['user_identity']
        if 'user_identity_type' in d:
            o.user_identity_type = d['user_identity_type']
        return o


