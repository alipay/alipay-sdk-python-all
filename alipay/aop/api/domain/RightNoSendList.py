#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RightNoSendList(object):

    def __init__(self):
        self._error_code = None
        self._error_message = None
        self._gift_prod_code = None
        self._right_no = None
        self._send_flow_no = None
        self._send_sum_insured = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def gift_prod_code(self):
        return self._gift_prod_code

    @gift_prod_code.setter
    def gift_prod_code(self, value):
        self._gift_prod_code = value
    @property
    def right_no(self):
        return self._right_no

    @right_no.setter
    def right_no(self, value):
        self._right_no = value
    @property
    def send_flow_no(self):
        return self._send_flow_no

    @send_flow_no.setter
    def send_flow_no(self, value):
        self._send_flow_no = value
    @property
    def send_sum_insured(self):
        return self._send_sum_insured

    @send_sum_insured.setter
    def send_sum_insured(self, value):
        self._send_sum_insured = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.gift_prod_code:
            if hasattr(self.gift_prod_code, 'to_alipay_dict'):
                params['gift_prod_code'] = self.gift_prod_code.to_alipay_dict()
            else:
                params['gift_prod_code'] = self.gift_prod_code
        if self.right_no:
            if hasattr(self.right_no, 'to_alipay_dict'):
                params['right_no'] = self.right_no.to_alipay_dict()
            else:
                params['right_no'] = self.right_no
        if self.send_flow_no:
            if hasattr(self.send_flow_no, 'to_alipay_dict'):
                params['send_flow_no'] = self.send_flow_no.to_alipay_dict()
            else:
                params['send_flow_no'] = self.send_flow_no
        if self.send_sum_insured:
            if hasattr(self.send_sum_insured, 'to_alipay_dict'):
                params['send_sum_insured'] = self.send_sum_insured.to_alipay_dict()
            else:
                params['send_sum_insured'] = self.send_sum_insured
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RightNoSendList()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'gift_prod_code' in d:
            o.gift_prod_code = d['gift_prod_code']
        if 'right_no' in d:
            o.right_no = d['right_no']
        if 'send_flow_no' in d:
            o.send_flow_no = d['send_flow_no']
        if 'send_sum_insured' in d:
            o.send_sum_insured = d['send_sum_insured']
        if 'success' in d:
            o.success = d['success']
        return o


