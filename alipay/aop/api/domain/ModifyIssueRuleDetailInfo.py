#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IssueRuleInfo import IssueRuleInfo
from alipay.aop.api.domain.ModifyIssueRuleInfo import ModifyIssueRuleInfo


class ModifyIssueRuleDetailInfo(object):

    def __init__(self):
        self._add_issue_rule_list = None
        self._delete_issue_rule_id_list = None
        self._modify_issue_rule_list = None

    @property
    def add_issue_rule_list(self):
        return self._add_issue_rule_list

    @add_issue_rule_list.setter
    def add_issue_rule_list(self, value):
        if isinstance(value, list):
            self._add_issue_rule_list = list()
            for i in value:
                if isinstance(i, IssueRuleInfo):
                    self._add_issue_rule_list.append(i)
                else:
                    self._add_issue_rule_list.append(IssueRuleInfo.from_alipay_dict(i))
    @property
    def delete_issue_rule_id_list(self):
        return self._delete_issue_rule_id_list

    @delete_issue_rule_id_list.setter
    def delete_issue_rule_id_list(self, value):
        if isinstance(value, list):
            self._delete_issue_rule_id_list = list()
            for i in value:
                self._delete_issue_rule_id_list.append(i)
    @property
    def modify_issue_rule_list(self):
        return self._modify_issue_rule_list

    @modify_issue_rule_list.setter
    def modify_issue_rule_list(self, value):
        if isinstance(value, ModifyIssueRuleInfo):
            self._modify_issue_rule_list = value
        else:
            self._modify_issue_rule_list = ModifyIssueRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.add_issue_rule_list:
            if isinstance(self.add_issue_rule_list, list):
                for i in range(0, len(self.add_issue_rule_list)):
                    element = self.add_issue_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_issue_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.add_issue_rule_list, 'to_alipay_dict'):
                params['add_issue_rule_list'] = self.add_issue_rule_list.to_alipay_dict()
            else:
                params['add_issue_rule_list'] = self.add_issue_rule_list
        if self.delete_issue_rule_id_list:
            if isinstance(self.delete_issue_rule_id_list, list):
                for i in range(0, len(self.delete_issue_rule_id_list)):
                    element = self.delete_issue_rule_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delete_issue_rule_id_list[i] = element.to_alipay_dict()
            if hasattr(self.delete_issue_rule_id_list, 'to_alipay_dict'):
                params['delete_issue_rule_id_list'] = self.delete_issue_rule_id_list.to_alipay_dict()
            else:
                params['delete_issue_rule_id_list'] = self.delete_issue_rule_id_list
        if self.modify_issue_rule_list:
            if hasattr(self.modify_issue_rule_list, 'to_alipay_dict'):
                params['modify_issue_rule_list'] = self.modify_issue_rule_list.to_alipay_dict()
            else:
                params['modify_issue_rule_list'] = self.modify_issue_rule_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModifyIssueRuleDetailInfo()
        if 'add_issue_rule_list' in d:
            o.add_issue_rule_list = d['add_issue_rule_list']
        if 'delete_issue_rule_id_list' in d:
            o.delete_issue_rule_id_list = d['delete_issue_rule_id_list']
        if 'modify_issue_rule_list' in d:
            o.modify_issue_rule_list = d['modify_issue_rule_list']
        return o


