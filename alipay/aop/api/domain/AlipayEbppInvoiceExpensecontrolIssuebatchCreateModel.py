#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IssueTargetInfoContent import IssueTargetInfoContent


class AlipayEbppInvoiceExpensecontrolIssuebatchCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._batch_no = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._enterprise_id = None
        self._institution_id = None
        self._issue_desc = None
        self._issue_name = None
        self._issue_target_info_list = None
        self._quota_type = None
        self._share_mode = None

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
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
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
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def issue_desc(self):
        return self._issue_desc

    @issue_desc.setter
    def issue_desc(self, value):
        self._issue_desc = value
    @property
    def issue_name(self):
        return self._issue_name

    @issue_name.setter
    def issue_name(self, value):
        self._issue_name = value
    @property
    def issue_target_info_list(self):
        return self._issue_target_info_list

    @issue_target_info_list.setter
    def issue_target_info_list(self, value):
        if isinstance(value, list):
            self._issue_target_info_list = list()
            for i in value:
                if isinstance(i, IssueTargetInfoContent):
                    self._issue_target_info_list.append(i)
                else:
                    self._issue_target_info_list.append(IssueTargetInfoContent.from_alipay_dict(i))
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
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
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
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.issue_desc:
            if hasattr(self.issue_desc, 'to_alipay_dict'):
                params['issue_desc'] = self.issue_desc.to_alipay_dict()
            else:
                params['issue_desc'] = self.issue_desc
        if self.issue_name:
            if hasattr(self.issue_name, 'to_alipay_dict'):
                params['issue_name'] = self.issue_name.to_alipay_dict()
            else:
                params['issue_name'] = self.issue_name
        if self.issue_target_info_list:
            if isinstance(self.issue_target_info_list, list):
                for i in range(0, len(self.issue_target_info_list)):
                    element = self.issue_target_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.issue_target_info_list[i] = element.to_alipay_dict()
            if hasattr(self.issue_target_info_list, 'to_alipay_dict'):
                params['issue_target_info_list'] = self.issue_target_info_list.to_alipay_dict()
            else:
                params['issue_target_info_list'] = self.issue_target_info_list
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
        o = AlipayEbppInvoiceExpensecontrolIssuebatchCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'issue_desc' in d:
            o.issue_desc = d['issue_desc']
        if 'issue_name' in d:
            o.issue_name = d['issue_name']
        if 'issue_target_info_list' in d:
            o.issue_target_info_list = d['issue_target_info_list']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        if 'share_mode' in d:
            o.share_mode = d['share_mode']
        return o


