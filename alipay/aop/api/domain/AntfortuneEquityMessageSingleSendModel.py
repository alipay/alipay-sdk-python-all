#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MessageTemplate import MessageTemplate


class AntfortuneEquityMessageSingleSendModel(object):

    def __init__(self):
        self._ta_code = None
        self._template = None
        self._trade_account = None

    @property
    def ta_code(self):
        return self._ta_code

    @ta_code.setter
    def ta_code(self, value):
        self._ta_code = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, MessageTemplate):
            self._template = value
        else:
            self._template = MessageTemplate.from_alipay_dict(value)
    @property
    def trade_account(self):
        return self._trade_account

    @trade_account.setter
    def trade_account(self, value):
        self._trade_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.ta_code:
            if hasattr(self.ta_code, 'to_alipay_dict'):
                params['ta_code'] = self.ta_code.to_alipay_dict()
            else:
                params['ta_code'] = self.ta_code
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        if self.trade_account:
            if hasattr(self.trade_account, 'to_alipay_dict'):
                params['trade_account'] = self.trade_account.to_alipay_dict()
            else:
                params['trade_account'] = self.trade_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneEquityMessageSingleSendModel()
        if 'ta_code' in d:
            o.ta_code = d['ta_code']
        if 'template' in d:
            o.template = d['template']
        if 'trade_account' in d:
            o.trade_account = d['trade_account']
        return o


