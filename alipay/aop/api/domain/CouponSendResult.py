#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponSendResult(object):

    def __init__(self):
        self._coupon_code = None
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._send_result = None

    @property
    def coupon_code(self):
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, value):
        self._coupon_code = value
    @property
    def fail_reason_code(self):
        return self._fail_reason_code

    @fail_reason_code.setter
    def fail_reason_code(self, value):
        self._fail_reason_code = value
    @property
    def fail_reason_message(self):
        return self._fail_reason_message

    @fail_reason_message.setter
    def fail_reason_message(self, value):
        self._fail_reason_message = value
    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_code:
            if hasattr(self.coupon_code, 'to_alipay_dict'):
                params['coupon_code'] = self.coupon_code.to_alipay_dict()
            else:
                params['coupon_code'] = self.coupon_code
        if self.fail_reason_code:
            if hasattr(self.fail_reason_code, 'to_alipay_dict'):
                params['fail_reason_code'] = self.fail_reason_code.to_alipay_dict()
            else:
                params['fail_reason_code'] = self.fail_reason_code
        if self.fail_reason_message:
            if hasattr(self.fail_reason_message, 'to_alipay_dict'):
                params['fail_reason_message'] = self.fail_reason_message.to_alipay_dict()
            else:
                params['fail_reason_message'] = self.fail_reason_message
        if self.send_result:
            if hasattr(self.send_result, 'to_alipay_dict'):
                params['send_result'] = self.send_result.to_alipay_dict()
            else:
                params['send_result'] = self.send_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponSendResult()
        if 'coupon_code' in d:
            o.coupon_code = d['coupon_code']
        if 'fail_reason_code' in d:
            o.fail_reason_code = d['fail_reason_code']
        if 'fail_reason_message' in d:
            o.fail_reason_message = d['fail_reason_message']
        if 'send_result' in d:
            o.send_result = d['send_result']
        return o


