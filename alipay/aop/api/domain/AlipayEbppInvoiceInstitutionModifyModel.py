#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ModifyIssueRuleDetailInfo import ModifyIssueRuleDetailInfo
from alipay.aop.api.domain.ModifyScopeInfo import ModifyScopeInfo
from alipay.aop.api.domain.ModifyStandardDetailInfo import ModifyStandardDetailInfo


class AlipayEbppInvoiceInstitutionModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._consult_mode = None
        self._effective = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._enterprise_id = None
        self._institution_desc = None
        self._institution_id = None
        self._institution_name = None
        self._modify_issue_rule_detail_info = None
        self._modify_scope_info = None
        self._modify_standard_detail_info = None

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
    def consult_mode(self):
        return self._consult_mode

    @consult_mode.setter
    def consult_mode(self, value):
        self._consult_mode = value
    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value
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
    def institution_desc(self):
        return self._institution_desc

    @institution_desc.setter
    def institution_desc(self, value):
        self._institution_desc = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def institution_name(self):
        return self._institution_name

    @institution_name.setter
    def institution_name(self, value):
        self._institution_name = value
    @property
    def modify_issue_rule_detail_info(self):
        return self._modify_issue_rule_detail_info

    @modify_issue_rule_detail_info.setter
    def modify_issue_rule_detail_info(self, value):
        if isinstance(value, ModifyIssueRuleDetailInfo):
            self._modify_issue_rule_detail_info = value
        else:
            self._modify_issue_rule_detail_info = ModifyIssueRuleDetailInfo.from_alipay_dict(value)
    @property
    def modify_scope_info(self):
        return self._modify_scope_info

    @modify_scope_info.setter
    def modify_scope_info(self, value):
        if isinstance(value, ModifyScopeInfo):
            self._modify_scope_info = value
        else:
            self._modify_scope_info = ModifyScopeInfo.from_alipay_dict(value)
    @property
    def modify_standard_detail_info(self):
        return self._modify_standard_detail_info

    @modify_standard_detail_info.setter
    def modify_standard_detail_info(self, value):
        if isinstance(value, ModifyStandardDetailInfo):
            self._modify_standard_detail_info = value
        else:
            self._modify_standard_detail_info = ModifyStandardDetailInfo.from_alipay_dict(value)


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
        if self.consult_mode:
            if hasattr(self.consult_mode, 'to_alipay_dict'):
                params['consult_mode'] = self.consult_mode.to_alipay_dict()
            else:
                params['consult_mode'] = self.consult_mode
        if self.effective:
            if hasattr(self.effective, 'to_alipay_dict'):
                params['effective'] = self.effective.to_alipay_dict()
            else:
                params['effective'] = self.effective
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
        if self.institution_desc:
            if hasattr(self.institution_desc, 'to_alipay_dict'):
                params['institution_desc'] = self.institution_desc.to_alipay_dict()
            else:
                params['institution_desc'] = self.institution_desc
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.institution_name:
            if hasattr(self.institution_name, 'to_alipay_dict'):
                params['institution_name'] = self.institution_name.to_alipay_dict()
            else:
                params['institution_name'] = self.institution_name
        if self.modify_issue_rule_detail_info:
            if hasattr(self.modify_issue_rule_detail_info, 'to_alipay_dict'):
                params['modify_issue_rule_detail_info'] = self.modify_issue_rule_detail_info.to_alipay_dict()
            else:
                params['modify_issue_rule_detail_info'] = self.modify_issue_rule_detail_info
        if self.modify_scope_info:
            if hasattr(self.modify_scope_info, 'to_alipay_dict'):
                params['modify_scope_info'] = self.modify_scope_info.to_alipay_dict()
            else:
                params['modify_scope_info'] = self.modify_scope_info
        if self.modify_standard_detail_info:
            if hasattr(self.modify_standard_detail_info, 'to_alipay_dict'):
                params['modify_standard_detail_info'] = self.modify_standard_detail_info.to_alipay_dict()
            else:
                params['modify_standard_detail_info'] = self.modify_standard_detail_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceInstitutionModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'consult_mode' in d:
            o.consult_mode = d['consult_mode']
        if 'effective' in d:
            o.effective = d['effective']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'institution_desc' in d:
            o.institution_desc = d['institution_desc']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'institution_name' in d:
            o.institution_name = d['institution_name']
        if 'modify_issue_rule_detail_info' in d:
            o.modify_issue_rule_detail_info = d['modify_issue_rule_detail_info']
        if 'modify_scope_info' in d:
            o.modify_scope_info = d['modify_scope_info']
        if 'modify_standard_detail_info' in d:
            o.modify_standard_detail_info = d['modify_standard_detail_info']
        return o


