#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationMessageHashSendModel(object):

    def __init__(self):
        self._context = None
        self._to_mobile_hash = None
        self._trigger_condition = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def to_mobile_hash(self):
        return self._to_mobile_hash

    @to_mobile_hash.setter
    def to_mobile_hash(self, value):
        self._to_mobile_hash = value
    @property
    def trigger_condition(self):
        return self._trigger_condition

    @trigger_condition.setter
    def trigger_condition(self, value):
        self._trigger_condition = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.to_mobile_hash:
            if hasattr(self.to_mobile_hash, 'to_alipay_dict'):
                params['to_mobile_hash'] = self.to_mobile_hash.to_alipay_dict()
            else:
                params['to_mobile_hash'] = self.to_mobile_hash
        if self.trigger_condition:
            if hasattr(self.trigger_condition, 'to_alipay_dict'):
                params['trigger_condition'] = self.trigger_condition.to_alipay_dict()
            else:
                params['trigger_condition'] = self.trigger_condition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationMessageHashSendModel()
        if 'context' in d:
            o.context = d['context']
        if 'to_mobile_hash' in d:
            o.to_mobile_hash = d['to_mobile_hash']
        if 'trigger_condition' in d:
            o.trigger_condition = d['trigger_condition']
        return o


