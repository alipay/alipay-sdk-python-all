#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmartphoneVendorsEventInfo(object):

    def __init__(self):
        self._event_code = None
        self._trigger_condition = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def trigger_condition(self):
        return self._trigger_condition

    @trigger_condition.setter
    def trigger_condition(self, value):
        self._trigger_condition = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
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
        o = SmartphoneVendorsEventInfo()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'trigger_condition' in d:
            o.trigger_condition = d['trigger_condition']
        return o


