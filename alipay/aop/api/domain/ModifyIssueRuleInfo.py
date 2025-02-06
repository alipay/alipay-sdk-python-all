#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ModifyIssueRuleInfo(object):

    def __init__(self):
        self._effective_period = None
        self._issue_rule_id = None
        self._issue_rule_name = None
        self._issue_type = None
        self._quota_type = None

    @property
    def effective_period(self):
        return self._effective_period

    @effective_period.setter
    def effective_period(self, value):
        self._effective_period = value
    @property
    def issue_rule_id(self):
        return self._issue_rule_id

    @issue_rule_id.setter
    def issue_rule_id(self, value):
        self._issue_rule_id = value
    @property
    def issue_rule_name(self):
        return self._issue_rule_name

    @issue_rule_name.setter
    def issue_rule_name(self, value):
        self._issue_rule_name = value
    @property
    def issue_type(self):
        return self._issue_type

    @issue_type.setter
    def issue_type(self, value):
        self._issue_type = value
    @property
    def quota_type(self):
        return self._quota_type

    @quota_type.setter
    def quota_type(self, value):
        self._quota_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_period:
            if hasattr(self.effective_period, 'to_alipay_dict'):
                params['effective_period'] = self.effective_period.to_alipay_dict()
            else:
                params['effective_period'] = self.effective_period
        if self.issue_rule_id:
            if hasattr(self.issue_rule_id, 'to_alipay_dict'):
                params['issue_rule_id'] = self.issue_rule_id.to_alipay_dict()
            else:
                params['issue_rule_id'] = self.issue_rule_id
        if self.issue_rule_name:
            if hasattr(self.issue_rule_name, 'to_alipay_dict'):
                params['issue_rule_name'] = self.issue_rule_name.to_alipay_dict()
            else:
                params['issue_rule_name'] = self.issue_rule_name
        if self.issue_type:
            if hasattr(self.issue_type, 'to_alipay_dict'):
                params['issue_type'] = self.issue_type.to_alipay_dict()
            else:
                params['issue_type'] = self.issue_type
        if self.quota_type:
            if hasattr(self.quota_type, 'to_alipay_dict'):
                params['quota_type'] = self.quota_type.to_alipay_dict()
            else:
                params['quota_type'] = self.quota_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModifyIssueRuleInfo()
        if 'effective_period' in d:
            o.effective_period = d['effective_period']
        if 'issue_rule_id' in d:
            o.issue_rule_id = d['issue_rule_id']
        if 'issue_rule_name' in d:
            o.issue_rule_name = d['issue_rule_name']
        if 'issue_type' in d:
            o.issue_type = d['issue_type']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        return o


