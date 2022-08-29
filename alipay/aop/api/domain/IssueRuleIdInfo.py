#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IssueRuleIdInfo(object):

    def __init__(self):
        self._issue_rule_id = None
        self._outer_source_id = None

    @property
    def issue_rule_id(self):
        return self._issue_rule_id

    @issue_rule_id.setter
    def issue_rule_id(self, value):
        self._issue_rule_id = value
    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.issue_rule_id:
            if hasattr(self.issue_rule_id, 'to_alipay_dict'):
                params['issue_rule_id'] = self.issue_rule_id.to_alipay_dict()
            else:
                params['issue_rule_id'] = self.issue_rule_id
        if self.outer_source_id:
            if hasattr(self.outer_source_id, 'to_alipay_dict'):
                params['outer_source_id'] = self.outer_source_id.to_alipay_dict()
            else:
                params['outer_source_id'] = self.outer_source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IssueRuleIdInfo()
        if 'issue_rule_id' in d:
            o.issue_rule_id = d['issue_rule_id']
        if 'outer_source_id' in d:
            o.outer_source_id = d['outer_source_id']
        return o


