#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceIssueruleDeleteModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._enterprise_id = None
        self._issue_rule_id_list = None
        self._target_id = None
        self._target_type = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def issue_rule_id_list(self):
        return self._issue_rule_id_list

    @issue_rule_id_list.setter
    def issue_rule_id_list(self, value):
        if isinstance(value, list):
            self._issue_rule_id_list = list()
            for i in value:
                self._issue_rule_id_list.append(i)
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
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.issue_rule_id_list:
            if isinstance(self.issue_rule_id_list, list):
                for i in range(0, len(self.issue_rule_id_list)):
                    element = self.issue_rule_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.issue_rule_id_list[i] = element.to_alipay_dict()
            if hasattr(self.issue_rule_id_list, 'to_alipay_dict'):
                params['issue_rule_id_list'] = self.issue_rule_id_list.to_alipay_dict()
            else:
                params['issue_rule_id_list'] = self.issue_rule_id_list
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
        o = AlipayEbppInvoiceIssueruleDeleteModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'issue_rule_id_list' in d:
            o.issue_rule_id_list = d['issue_rule_id_list']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


