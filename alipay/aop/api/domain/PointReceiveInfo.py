#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointReceiveInfo(object):

    def __init__(self):
        self._msg = None
        self._received_point_amount = None
        self._result = None

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def received_point_amount(self):
        return self._received_point_amount

    @received_point_amount.setter
    def received_point_amount(self, value):
        self._received_point_amount = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.received_point_amount:
            if hasattr(self.received_point_amount, 'to_alipay_dict'):
                params['received_point_amount'] = self.received_point_amount.to_alipay_dict()
            else:
                params['received_point_amount'] = self.received_point_amount
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointReceiveInfo()
        if 'msg' in d:
            o.msg = d['msg']
        if 'received_point_amount' in d:
            o.received_point_amount = d['received_point_amount']
        if 'result' in d:
            o.result = d['result']
        return o


