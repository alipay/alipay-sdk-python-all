#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntlescenterFileDTO import AntlescenterFileDTO


class AlipayBossAntlescenterPartcontractreviewApplyModel(object):

    def __init__(self):
        self._audit_url = None
        self._audit_work_no = None
        self._company_list = None
        self._contract_no = None
        self._other_contract_file_addr = None
        self._tenant = None

    @property
    def audit_url(self):
        return self._audit_url

    @audit_url.setter
    def audit_url(self, value):
        self._audit_url = value
    @property
    def audit_work_no(self):
        return self._audit_work_no

    @audit_work_no.setter
    def audit_work_no(self, value):
        self._audit_work_no = value
    @property
    def company_list(self):
        return self._company_list

    @company_list.setter
    def company_list(self, value):
        if isinstance(value, list):
            self._company_list = list()
            for i in value:
                self._company_list.append(i)
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def other_contract_file_addr(self):
        return self._other_contract_file_addr

    @other_contract_file_addr.setter
    def other_contract_file_addr(self, value):
        if isinstance(value, AntlescenterFileDTO):
            self._other_contract_file_addr = value
        else:
            self._other_contract_file_addr = AntlescenterFileDTO.from_alipay_dict(value)
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_url:
            if hasattr(self.audit_url, 'to_alipay_dict'):
                params['audit_url'] = self.audit_url.to_alipay_dict()
            else:
                params['audit_url'] = self.audit_url
        if self.audit_work_no:
            if hasattr(self.audit_work_no, 'to_alipay_dict'):
                params['audit_work_no'] = self.audit_work_no.to_alipay_dict()
            else:
                params['audit_work_no'] = self.audit_work_no
        if self.company_list:
            if isinstance(self.company_list, list):
                for i in range(0, len(self.company_list)):
                    element = self.company_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_list[i] = element.to_alipay_dict()
            if hasattr(self.company_list, 'to_alipay_dict'):
                params['company_list'] = self.company_list.to_alipay_dict()
            else:
                params['company_list'] = self.company_list
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.other_contract_file_addr:
            if hasattr(self.other_contract_file_addr, 'to_alipay_dict'):
                params['other_contract_file_addr'] = self.other_contract_file_addr.to_alipay_dict()
            else:
                params['other_contract_file_addr'] = self.other_contract_file_addr
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossAntlescenterPartcontractreviewApplyModel()
        if 'audit_url' in d:
            o.audit_url = d['audit_url']
        if 'audit_work_no' in d:
            o.audit_work_no = d['audit_work_no']
        if 'company_list' in d:
            o.company_list = d['company_list']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'other_contract_file_addr' in d:
            o.other_contract_file_addr = d['other_contract_file_addr']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


