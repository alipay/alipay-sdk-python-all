#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityPayeeinfoCreateModel(object):

    def __init__(self):
        self._payee_pid = None
        self._payee_settle_mode = None

    @property
    def payee_pid(self):
        return self._payee_pid

    @payee_pid.setter
    def payee_pid(self, value):
        self._payee_pid = value
    @property
    def payee_settle_mode(self):
        return self._payee_settle_mode

    @payee_settle_mode.setter
    def payee_settle_mode(self, value):
        self._payee_settle_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee_pid:
            if hasattr(self.payee_pid, 'to_alipay_dict'):
                params['payee_pid'] = self.payee_pid.to_alipay_dict()
            else:
                params['payee_pid'] = self.payee_pid
        if self.payee_settle_mode:
            if hasattr(self.payee_settle_mode, 'to_alipay_dict'):
                params['payee_settle_mode'] = self.payee_settle_mode.to_alipay_dict()
            else:
                params['payee_settle_mode'] = self.payee_settle_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityPayeeinfoCreateModel()
        if 'payee_pid' in d:
            o.payee_pid = d['payee_pid']
        if 'payee_settle_mode' in d:
            o.payee_settle_mode = d['payee_settle_mode']
        return o


