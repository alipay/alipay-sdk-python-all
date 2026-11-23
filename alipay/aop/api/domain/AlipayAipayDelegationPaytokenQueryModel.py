#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayDelegationPaytokenQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._merchant_pid = None
        self._pay_token = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def pay_token(self):
        return self._pay_token

    @pay_token.setter
    def pay_token(self, value):
        self._pay_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.pay_token:
            if hasattr(self.pay_token, 'to_alipay_dict'):
                params['pay_token'] = self.pay_token.to_alipay_dict()
            else:
                params['pay_token'] = self.pay_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayDelegationPaytokenQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'pay_token' in d:
            o.pay_token = d['pay_token']
        return o


