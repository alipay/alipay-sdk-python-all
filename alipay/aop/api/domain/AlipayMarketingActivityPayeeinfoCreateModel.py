#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityPayeeinfoCreateModel(object):

    def __init__(self):
        self._payee_pid = None

    @property
    def payee_pid(self):
        return self._payee_pid

    @payee_pid.setter
    def payee_pid(self, value):
        self._payee_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee_pid:
            if hasattr(self.payee_pid, 'to_alipay_dict'):
                params['payee_pid'] = self.payee_pid.to_alipay_dict()
            else:
                params['payee_pid'] = self.payee_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityPayeeinfoCreateModel()
        if 'payee_pid' in d:
            o.payee_pid = d['payee_pid']
        return o


