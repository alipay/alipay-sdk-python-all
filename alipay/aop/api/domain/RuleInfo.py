#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleInfo(object):

    def __init__(self):
        self._attention_level = None
        self._comment = None
        self._mark_result = None
        self._risk_level = None
        self._risk_tips = None
        self._rule_code = None
        self._rule_name = None
        self._status = None

    @property
    def attention_level(self):
        return self._attention_level

    @attention_level.setter
    def attention_level(self, value):
        self._attention_level = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def mark_result(self):
        return self._mark_result

    @mark_result.setter
    def mark_result(self, value):
        self._mark_result = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_tips(self):
        return self._risk_tips

    @risk_tips.setter
    def risk_tips(self, value):
        self._risk_tips = value
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.attention_level:
            if hasattr(self.attention_level, 'to_alipay_dict'):
                params['attention_level'] = self.attention_level.to_alipay_dict()
            else:
                params['attention_level'] = self.attention_level
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.mark_result:
            if hasattr(self.mark_result, 'to_alipay_dict'):
                params['mark_result'] = self.mark_result.to_alipay_dict()
            else:
                params['mark_result'] = self.mark_result
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_tips:
            if hasattr(self.risk_tips, 'to_alipay_dict'):
                params['risk_tips'] = self.risk_tips.to_alipay_dict()
            else:
                params['risk_tips'] = self.risk_tips
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleInfo()
        if 'attention_level' in d:
            o.attention_level = d['attention_level']
        if 'comment' in d:
            o.comment = d['comment']
        if 'mark_result' in d:
            o.mark_result = d['mark_result']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_tips' in d:
            o.risk_tips = d['risk_tips']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'status' in d:
            o.status = d['status']
        return o


