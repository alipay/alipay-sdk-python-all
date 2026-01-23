#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultFailReason(object):

    def __init__(self):
        self._fail_code = None
        self._fail_message = None

    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_message:
            if hasattr(self.fail_message, 'to_alipay_dict'):
                params['fail_message'] = self.fail_message.to_alipay_dict()
            else:
                params['fail_message'] = self.fail_message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultFailReason()
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_message' in d:
            o.fail_message = d['fail_message']
        return o


