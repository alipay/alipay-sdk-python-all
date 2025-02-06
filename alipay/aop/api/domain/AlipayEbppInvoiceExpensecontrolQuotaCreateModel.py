#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IssueTargetInfoContent import IssueTargetInfoContent


class AlipayEbppInvoiceExpensecontrolQuotaCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._enterprise_id = None
        self._issue_desc = None
        self._issue_name = None
        self._issue_quota_target_list = None
        self._outer_source_id = None
        self._owner_id = None
        self._owner_open_id = None
        self._owner_type = None
        self._platform = None
        self._quota_type = None
        self._quota_value = None
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
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
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
    def issue_quota_target_list(self):
        return self._issue_quota_target_list

    @issue_quota_target_list.setter
    def issue_quota_target_list(self, value):
        if isinstance(value, list):
            self._issue_quota_target_list = list()
            for i in value:
                if isinstance(i, IssueTargetInfoContent):
                    self._issue_quota_target_list.append(i)
                else:
                    self._issue_quota_target_list.append(IssueTargetInfoContent.from_alipay_dict(i))
    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_open_id(self):
        return self._owner_open_id

    @owner_open_id.setter
    def owner_open_id(self, value):
        self._owner_open_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def quota_type(self):
        return self._quota_type

    @quota_type.setter
    def quota_type(self, value):
        self._quota_type = value
    @property
    def quota_value(self):
        return self._quota_value

    @quota_value.setter
    def quota_value(self, value):
        self._quota_value = value
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
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
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
        if self.issue_quota_target_list:
            if isinstance(self.issue_quota_target_list, list):
                for i in range(0, len(self.issue_quota_target_list)):
                    element = self.issue_quota_target_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.issue_quota_target_list[i] = element.to_alipay_dict()
            if hasattr(self.issue_quota_target_list, 'to_alipay_dict'):
                params['issue_quota_target_list'] = self.issue_quota_target_list.to_alipay_dict()
            else:
                params['issue_quota_target_list'] = self.issue_quota_target_list
        if self.outer_source_id:
            if hasattr(self.outer_source_id, 'to_alipay_dict'):
                params['outer_source_id'] = self.outer_source_id.to_alipay_dict()
            else:
                params['outer_source_id'] = self.outer_source_id
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_open_id:
            if hasattr(self.owner_open_id, 'to_alipay_dict'):
                params['owner_open_id'] = self.owner_open_id.to_alipay_dict()
            else:
                params['owner_open_id'] = self.owner_open_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.quota_type:
            if hasattr(self.quota_type, 'to_alipay_dict'):
                params['quota_type'] = self.quota_type.to_alipay_dict()
            else:
                params['quota_type'] = self.quota_type
        if self.quota_value:
            if hasattr(self.quota_value, 'to_alipay_dict'):
                params['quota_value'] = self.quota_value.to_alipay_dict()
            else:
                params['quota_value'] = self.quota_value
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
        o = AlipayEbppInvoiceExpensecontrolQuotaCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'issue_desc' in d:
            o.issue_desc = d['issue_desc']
        if 'issue_name' in d:
            o.issue_name = d['issue_name']
        if 'issue_quota_target_list' in d:
            o.issue_quota_target_list = d['issue_quota_target_list']
        if 'outer_source_id' in d:
            o.outer_source_id = d['outer_source_id']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_open_id' in d:
            o.owner_open_id = d['owner_open_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'platform' in d:
            o.platform = d['platform']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        if 'quota_value' in d:
            o.quota_value = d['quota_value']
        if 'share_mode' in d:
            o.share_mode = d['share_mode']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


