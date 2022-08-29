#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceIssueruleModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._action = None
        self._agreement_no = None
        self._effective = None
        self._effective_period = None
        self._enterprise_id = None
        self._invalid_mode = None
        self._invalid_mode_value = None
        self._issue_amount_value = None
        self._issue_end_date = None
        self._issue_rule_id = None
        self._issue_rule_name = None
        self._issue_start_date = None
        self._issue_type = None
        self._quota_type = None
        self._share_mode = None
        self._target_id = None
        self._target_type = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value
    @property
    def effective_period(self):
        return self._effective_period

    @effective_period.setter
    def effective_period(self, value):
        self._effective_period = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
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
    def issue_end_date(self):
        return self._issue_end_date

    @issue_end_date.setter
    def issue_end_date(self, value):
        self._issue_end_date = value
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
    def issue_start_date(self):
        return self._issue_start_date

    @issue_start_date.setter
    def issue_start_date(self, value):
        self._issue_start_date = value
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
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.effective:
            if hasattr(self.effective, 'to_alipay_dict'):
                params['effective'] = self.effective.to_alipay_dict()
            else:
                params['effective'] = self.effective
        if self.effective_period:
            if hasattr(self.effective_period, 'to_alipay_dict'):
                params['effective_period'] = self.effective_period.to_alipay_dict()
            else:
                params['effective_period'] = self.effective_period
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
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
        if self.issue_end_date:
            if hasattr(self.issue_end_date, 'to_alipay_dict'):
                params['issue_end_date'] = self.issue_end_date.to_alipay_dict()
            else:
                params['issue_end_date'] = self.issue_end_date
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
        if self.issue_start_date:
            if hasattr(self.issue_start_date, 'to_alipay_dict'):
                params['issue_start_date'] = self.issue_start_date.to_alipay_dict()
            else:
                params['issue_start_date'] = self.issue_start_date
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
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceIssueruleModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'action' in d:
            o.action = d['action']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'effective' in d:
            o.effective = d['effective']
        if 'effective_period' in d:
            o.effective_period = d['effective_period']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'invalid_mode' in d:
            o.invalid_mode = d['invalid_mode']
        if 'invalid_mode_value' in d:
            o.invalid_mode_value = d['invalid_mode_value']
        if 'issue_amount_value' in d:
            o.issue_amount_value = d['issue_amount_value']
        if 'issue_end_date' in d:
            o.issue_end_date = d['issue_end_date']
        if 'issue_rule_id' in d:
            o.issue_rule_id = d['issue_rule_id']
        if 'issue_rule_name' in d:
            o.issue_rule_name = d['issue_rule_name']
        if 'issue_start_date' in d:
            o.issue_start_date = d['issue_start_date']
        if 'issue_type' in d:
            o.issue_type = d['issue_type']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        if 'share_mode' in d:
            o.share_mode = d['share_mode']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


