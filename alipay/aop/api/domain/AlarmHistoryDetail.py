#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmHistoryDetail(object):

    def __init__(self):
        self._alarm_content = None
        self._alarm_time = None
        self._history_id = None
        self._rule_id = None

    @property
    def alarm_content(self):
        return self._alarm_content

    @alarm_content.setter
    def alarm_content(self, value):
        self._alarm_content = value
    @property
    def alarm_time(self):
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, value):
        self._alarm_time = value
    @property
    def history_id(self):
        return self._history_id

    @history_id.setter
    def history_id(self, value):
        self._history_id = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_content:
            if hasattr(self.alarm_content, 'to_alipay_dict'):
                params['alarm_content'] = self.alarm_content.to_alipay_dict()
            else:
                params['alarm_content'] = self.alarm_content
        if self.alarm_time:
            if hasattr(self.alarm_time, 'to_alipay_dict'):
                params['alarm_time'] = self.alarm_time.to_alipay_dict()
            else:
                params['alarm_time'] = self.alarm_time
        if self.history_id:
            if hasattr(self.history_id, 'to_alipay_dict'):
                params['history_id'] = self.history_id.to_alipay_dict()
            else:
                params['history_id'] = self.history_id
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmHistoryDetail()
        if 'alarm_content' in d:
            o.alarm_content = d['alarm_content']
        if 'alarm_time' in d:
            o.alarm_time = d['alarm_time']
        if 'history_id' in d:
            o.history_id = d['history_id']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        return o


