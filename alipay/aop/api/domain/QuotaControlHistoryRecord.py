#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuotaControlHistoryRecord(object):

    def __init__(self):
        self._fee_item_code = None
        self._operate_time = None
        self._rule_id = None
        self._threshold = None
        self._trigger_value = None

    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value
    @property
    def trigger_value(self):
        return self._trigger_value

    @trigger_value.setter
    def trigger_value(self, value):
        self._trigger_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.threshold:
            if hasattr(self.threshold, 'to_alipay_dict'):
                params['threshold'] = self.threshold.to_alipay_dict()
            else:
                params['threshold'] = self.threshold
        if self.trigger_value:
            if hasattr(self.trigger_value, 'to_alipay_dict'):
                params['trigger_value'] = self.trigger_value.to_alipay_dict()
            else:
                params['trigger_value'] = self.trigger_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuotaControlHistoryRecord()
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'threshold' in d:
            o.threshold = d['threshold']
        if 'trigger_value' in d:
            o.trigger_value = d['trigger_value']
        return o


