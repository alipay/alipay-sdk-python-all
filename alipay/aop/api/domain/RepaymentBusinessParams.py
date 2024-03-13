#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymentBusinessParams(object):

    def __init__(self):
        self._withdraw_timeliness = None

    @property
    def withdraw_timeliness(self):
        return self._withdraw_timeliness

    @withdraw_timeliness.setter
    def withdraw_timeliness(self, value):
        self._withdraw_timeliness = value


    def to_alipay_dict(self):
        params = dict()
        if self.withdraw_timeliness:
            if hasattr(self.withdraw_timeliness, 'to_alipay_dict'):
                params['withdraw_timeliness'] = self.withdraw_timeliness.to_alipay_dict()
            else:
                params['withdraw_timeliness'] = self.withdraw_timeliness
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepaymentBusinessParams()
        if 'withdraw_timeliness' in d:
            o.withdraw_timeliness = d['withdraw_timeliness']
        return o


