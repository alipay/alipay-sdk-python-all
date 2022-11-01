#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIoteopAlarmSendModel(object):

    def __init__(self):
        self._alarm_rule_id = None
        self._content = None
        self._sequence_diagram_id = None

    @property
    def alarm_rule_id(self):
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, value):
        self._alarm_rule_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def sequence_diagram_id(self):
        return self._sequence_diagram_id

    @sequence_diagram_id.setter
    def sequence_diagram_id(self, value):
        self._sequence_diagram_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_rule_id:
            if hasattr(self.alarm_rule_id, 'to_alipay_dict'):
                params['alarm_rule_id'] = self.alarm_rule_id.to_alipay_dict()
            else:
                params['alarm_rule_id'] = self.alarm_rule_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.sequence_diagram_id:
            if hasattr(self.sequence_diagram_id, 'to_alipay_dict'):
                params['sequence_diagram_id'] = self.sequence_diagram_id.to_alipay_dict()
            else:
                params['sequence_diagram_id'] = self.sequence_diagram_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIoteopAlarmSendModel()
        if 'alarm_rule_id' in d:
            o.alarm_rule_id = d['alarm_rule_id']
        if 'content' in d:
            o.content = d['content']
        if 'sequence_diagram_id' in d:
            o.sequence_diagram_id = d['sequence_diagram_id']
        return o


