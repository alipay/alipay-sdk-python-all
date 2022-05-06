#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleMarkInfo(object):

    def __init__(self):
        self._comment = None
        self._mark_result = None
        self._rule_code = None
        self._status = None

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
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
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
        o = RuleMarkInfo()
        if 'comment' in d:
            o.comment = d['comment']
        if 'mark_result' in d:
            o.mark_result = d['mark_result']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'status' in d:
            o.status = d['status']
        return o


