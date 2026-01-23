#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ModifyIssueRuleInfo(object):

    def __init__(self):
        self._effective_period = None
        self._invalid_mode = None
        self._invalid_mode_value = None
        self._issue_amount_value = None
        self._issue_rule_id = None
        self._issue_rule_name = None
        self._issue_type = None
        self._quota_type = None
        self._share_mode = None

    @property
    def effective_period(self):
        return self._effective_period

    @effective_period.setter
    def effective_period(self, value):
        self._effective_period = value
    @property
    def invalid_mode(self):
        return self._invalid_mode

    @invalid_mode.setter
    def invalid_mode(self, value):
        self._invalid_mode = value
    @property
    def invalid_mode_value(self):
        return self._invalid_mode_value

    @invalid_mode_value.setter
    def invalid_mode_value(self, value):
        self._invalid_mode_value = value
    @property
    def issue_amount_value(self):
        return self._issue_amount_value

    @issue_amount_value.setter
    def issue_amount_value(self, value):
        self._issue_amount_value = value
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
    @property
    def share_mode(self):
        return self._share_mode

    @share_mode.setter
    def share_mode(self, value):
        self._share_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_period:
            if hasattr(self.effective_period, 'to_alipay_dict'):
                params['effective_period'] = self.effective_period.to_alipay_dict()
            else:
                params['effective_period'] = self.effective_period
        if self.invalid_mode:
            if hasattr(self.invalid_mode, 'to_alipay_dict'):
                params['invalid_mode'] = self.invalid_mode.to_alipay_dict()
            else:
                params['invalid_mode'] = self.invalid_mode
        if self.invalid_mode_value:
            if hasattr(self.invalid_mode_value, 'to_alipay_dict'):
                params['invalid_mode_value'] = self.invalid_mode_value.to_alipay_dict()
            else:
                params['invalid_mode_value'] = self.invalid_mode_value
        if self.issue_amount_value:
            if hasattr(self.issue_amount_value, 'to_alipay_dict'):
                params['issue_amount_value'] = self.issue_amount_value.to_alipay_dict()
            else:
                params['issue_amount_value'] = self.issue_amount_value
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
        if self.share_mode:
            if hasattr(self.share_mode, 'to_alipay_dict'):
                params['share_mode'] = self.share_mode.to_alipay_dict()
            else:
                params['share_mode'] = self.share_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModifyIssueRuleInfo()
        if 'effective_period' in d:
            o.effective_period = d['effective_period']
        if 'invalid_mode' in d:
            o.invalid_mode = d['invalid_mode']
        if 'invalid_mode_value' in d:
            o.invalid_mode_value = d['invalid_mode_value']
        if 'issue_amount_value' in d:
            o.issue_amount_value = d['issue_amount_value']
        if 'issue_rule_id' in d:
            o.issue_rule_id = d['issue_rule_id']
        if 'issue_rule_name' in d:
            o.issue_rule_name = d['issue_rule_name']
        if 'issue_type' in d:
            o.issue_type = d['issue_type']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        if 'share_mode' in d:
            o.share_mode = d['share_mode']
        return o


