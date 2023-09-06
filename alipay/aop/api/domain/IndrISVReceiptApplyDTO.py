#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndrISVReceiptApplyDTO(object):

    def __init__(self):
        self._email = None
        self._pre_order_id = None
        self._receipt_type = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def receipt_type(self):
        return self._receipt_type

    @receipt_type.setter
    def receipt_type(self, value):
        self._receipt_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.receipt_type:
            if hasattr(self.receipt_type, 'to_alipay_dict'):
                params['receipt_type'] = self.receipt_type.to_alipay_dict()
            else:
                params['receipt_type'] = self.receipt_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVReceiptApplyDTO()
        if 'email' in d:
            o.email = d['email']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'receipt_type' in d:
            o.receipt_type = d['receipt_type']
        return o


