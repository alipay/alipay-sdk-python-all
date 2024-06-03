#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayInfoResponse(object):

    def __init__(self):
        self._no_pay_close_time = None

    @property
    def no_pay_close_time(self):
        return self._no_pay_close_time

    @no_pay_close_time.setter
    def no_pay_close_time(self, value):
        self._no_pay_close_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.no_pay_close_time:
            if hasattr(self.no_pay_close_time, 'to_alipay_dict'):
                params['no_pay_close_time'] = self.no_pay_close_time.to_alipay_dict()
            else:
                params['no_pay_close_time'] = self.no_pay_close_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayInfoResponse()
        if 'no_pay_close_time' in d:
            o.no_pay_close_time = d['no_pay_close_time']
        return o


