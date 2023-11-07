#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IssueRuleInfo import IssueRuleInfo
from alipay.aop.api.domain.StandardInfo import StandardInfo


class AlipayEbppInvoiceInstitutionCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._adapter_type = None
        self._agreement_no = None
        self._consult_mode = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._enterprise_id = None
        self._expense_type = None
        self._institution_desc = None
        self._institution_name = None
        self._issue_rule_info_list = None
        self._outer_source_id = None
        self._owner_id_list = None
        self._owner_open_id_list = None
        self._owner_type = None
        self._scene_type = None
        self._standard_info_list = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def adapter_type(self):
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, value):
        self._adapter_type = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def consult_mode(self):
        return self._consult_mode

    @consult_mode.setter
    def consult_mode(self, value):
        self._consult_mode = value
    @property
    def effective_end_date(self):
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, value):
        self._effective_end_date = value
    @property
    def effective_start_date(self):
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, value):
        self._effective_start_date = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def institution_desc(self):
        return self._institution_desc

    @institution_desc.setter
    def institution_desc(self, value):
        self._institution_desc = value
    @property
    def institution_name(self):
        return self._institution_name

    @institution_name.setter
    def institution_name(self, value):
        self._institution_name = value
    @property
    def issue_rule_info_list(self):
        return self._issue_rule_info_list

    @issue_rule_info_list.setter
    def issue_rule_info_list(self, value):
        if isinstance(value, list):
            self._issue_rule_info_list = list()
            for i in value:
                if isinstance(i, IssueRuleInfo):
                    self._issue_rule_info_list.append(i)
                else:
                    self._issue_rule_info_list.append(IssueRuleInfo.from_alipay_dict(i))
    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value
    @property
    def owner_id_list(self):
        return self._owner_id_list

    @owner_id_list.setter
    def owner_id_list(self, value):
        if isinstance(value, list):
            self._owner_id_list = list()
            for i in value:
                self._owner_id_list.append(i)
    @property
    def owner_open_id_list(self):
        return self._owner_open_id_list

    @owner_open_id_list.setter
    def owner_open_id_list(self, value):
        if isinstance(value, list):
            self._owner_open_id_list = list()
            for i in value:
                self._owner_open_id_list.append(i)
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def standard_info_list(self):
        return self._standard_info_list

    @standard_info_list.setter
    def standard_info_list(self, value):
        if isinstance(value, list):
            self._standard_info_list = list()
            for i in value:
                if isinstance(i, StandardInfo):
                    self._standard_info_list.append(i)
                else:
                    self._standard_info_list.append(StandardInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.adapter_type:
            if hasattr(self.adapter_type, 'to_alipay_dict'):
                params['adapter_type'] = self.adapter_type.to_alipay_dict()
            else:
                params['adapter_type'] = self.adapter_type
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.consult_mode:
            if hasattr(self.consult_mode, 'to_alipay_dict'):
                params['consult_mode'] = self.consult_mode.to_alipay_dict()
            else:
                params['consult_mode'] = self.consult_mode
        if self.effective_end_date:
            if hasattr(self.effective_end_date, 'to_alipay_dict'):
                params['effective_end_date'] = self.effective_end_date.to_alipay_dict()
            else:
                params['effective_end_date'] = self.effective_end_date
        if self.effective_start_date:
            if hasattr(self.effective_start_date, 'to_alipay_dict'):
                params['effective_start_date'] = self.effective_start_date.to_alipay_dict()
            else:
                params['effective_start_date'] = self.effective_start_date
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_type:
            if hasattr(self.expense_type, 'to_alipay_dict'):
                params['expense_type'] = self.expense_type.to_alipay_dict()
            else:
                params['expense_type'] = self.expense_type
        if self.institution_desc:
            if hasattr(self.institution_desc, 'to_alipay_dict'):
                params['institution_desc'] = self.institution_desc.to_alipay_dict()
            else:
                params['institution_desc'] = self.institution_desc
        if self.institution_name:
            if hasattr(self.institution_name, 'to_alipay_dict'):
                params['institution_name'] = self.institution_name.to_alipay_dict()
            else:
                params['institution_name'] = self.institution_name
        if self.issue_rule_info_list:
            if isinstance(self.issue_rule_info_list, list):
                for i in range(0, len(self.issue_rule_info_list)):
                    element = self.issue_rule_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.issue_rule_info_list[i] = element.to_alipay_dict()
            if hasattr(self.issue_rule_info_list, 'to_alipay_dict'):
                params['issue_rule_info_list'] = self.issue_rule_info_list.to_alipay_dict()
            else:
                params['issue_rule_info_list'] = self.issue_rule_info_list
        if self.outer_source_id:
            if hasattr(self.outer_source_id, 'to_alipay_dict'):
                params['outer_source_id'] = self.outer_source_id.to_alipay_dict()
            else:
                params['outer_source_id'] = self.outer_source_id
        if self.owner_id_list:
            if isinstance(self.owner_id_list, list):
                for i in range(0, len(self.owner_id_list)):
                    element = self.owner_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.owner_id_list[i] = element.to_alipay_dict()
            if hasattr(self.owner_id_list, 'to_alipay_dict'):
                params['owner_id_list'] = self.owner_id_list.to_alipay_dict()
            else:
                params['owner_id_list'] = self.owner_id_list
        if self.owner_open_id_list:
            if isinstance(self.owner_open_id_list, list):
                for i in range(0, len(self.owner_open_id_list)):
                    element = self.owner_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.owner_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.owner_open_id_list, 'to_alipay_dict'):
                params['owner_open_id_list'] = self.owner_open_id_list.to_alipay_dict()
            else:
                params['owner_open_id_list'] = self.owner_open_id_list
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.standard_info_list:
            if isinstance(self.standard_info_list, list):
                for i in range(0, len(self.standard_info_list)):
                    element = self.standard_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_info_list[i] = element.to_alipay_dict()
            if hasattr(self.standard_info_list, 'to_alipay_dict'):
                params['standard_info_list'] = self.standard_info_list.to_alipay_dict()
            else:
                params['standard_info_list'] = self.standard_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceInstitutionCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'adapter_type' in d:
            o.adapter_type = d['adapter_type']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'consult_mode' in d:
            o.consult_mode = d['consult_mode']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'institution_desc' in d:
            o.institution_desc = d['institution_desc']
        if 'institution_name' in d:
            o.institution_name = d['institution_name']
        if 'issue_rule_info_list' in d:
            o.issue_rule_info_list = d['issue_rule_info_list']
        if 'outer_source_id' in d:
            o.outer_source_id = d['outer_source_id']
        if 'owner_id_list' in d:
            o.owner_id_list = d['owner_id_list']
        if 'owner_open_id_list' in d:
            o.owner_open_id_list = d['owner_open_id_list']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'standard_info_list' in d:
            o.standard_info_list = d['standard_info_list']
        return o


