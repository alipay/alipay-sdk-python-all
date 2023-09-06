#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndrISVReceiptApplyResultDTO(object):

    def __init__(self):
        self._apply_result_code = None
        self._apply_result_message = None
        self._email = None
        self._pre_order_id = None
        self._receipt_type = None

    @property
    def apply_result_code(self):
        return self._apply_result_code

    @apply_result_code.setter
    def apply_result_code(self, value):
        self._apply_result_code = value
    @property
    def apply_result_message(self):
        return self._apply_result_message

    @apply_result_message.setter
    def apply_result_message(self, value):
        self._apply_result_message = value
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
        if self.apply_result_code:
            if hasattr(self.apply_result_code, 'to_alipay_dict'):
                params['apply_result_code'] = self.apply_result_code.to_alipay_dict()
            else:
                params['apply_result_code'] = self.apply_result_code
        if self.apply_result_message:
            if hasattr(self.apply_result_message, 'to_alipay_dict'):
                params['apply_result_message'] = self.apply_result_message.to_alipay_dict()
            else:
                params['apply_result_message'] = self.apply_result_message
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
        o = IndrISVReceiptApplyResultDTO()
        if 'apply_result_code' in d:
            o.apply_result_code = d['apply_result_code']
        if 'apply_result_message' in d:
            o.apply_result_message = d['apply_result_message']
        if 'email' in d:
            o.email = d['email']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'receipt_type' in d:
            o.receipt_type = d['receipt_type']
        return o


