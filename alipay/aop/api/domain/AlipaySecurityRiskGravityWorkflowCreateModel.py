#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskGravityWorkflowCreateModel(object):

    def __init__(self):
        self._auth_feature_tables = None
        self._check_sample_tables = None
        self._contract_id = None
        self._description = None
        self._domain_account = None
        self._org_info = None
        self._project_id = None
        self._project_name = None
        self._review_history = None

    @property
    def auth_feature_tables(self):
        return self._auth_feature_tables

    @auth_feature_tables.setter
    def auth_feature_tables(self, value):
        self._auth_feature_tables = value
    @property
    def check_sample_tables(self):
        return self._check_sample_tables

    @check_sample_tables.setter
    def check_sample_tables(self, value):
        self._check_sample_tables = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def domain_account(self):
        return self._domain_account

    @domain_account.setter
    def domain_account(self, value):
        self._domain_account = value
    @property
    def org_info(self):
        return self._org_info

    @org_info.setter
    def org_info(self, value):
        self._org_info = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def review_history(self):
        return self._review_history

    @review_history.setter
    def review_history(self, value):
        self._review_history = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_feature_tables:
            if hasattr(self.auth_feature_tables, 'to_alipay_dict'):
                params['auth_feature_tables'] = self.auth_feature_tables.to_alipay_dict()
            else:
                params['auth_feature_tables'] = self.auth_feature_tables
        if self.check_sample_tables:
            if hasattr(self.check_sample_tables, 'to_alipay_dict'):
                params['check_sample_tables'] = self.check_sample_tables.to_alipay_dict()
            else:
                params['check_sample_tables'] = self.check_sample_tables
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.domain_account:
            if hasattr(self.domain_account, 'to_alipay_dict'):
                params['domain_account'] = self.domain_account.to_alipay_dict()
            else:
                params['domain_account'] = self.domain_account
        if self.org_info:
            if hasattr(self.org_info, 'to_alipay_dict'):
                params['org_info'] = self.org_info.to_alipay_dict()
            else:
                params['org_info'] = self.org_info
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.review_history:
            if hasattr(self.review_history, 'to_alipay_dict'):
                params['review_history'] = self.review_history.to_alipay_dict()
            else:
                params['review_history'] = self.review_history
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskGravityWorkflowCreateModel()
        if 'auth_feature_tables' in d:
            o.auth_feature_tables = d['auth_feature_tables']
        if 'check_sample_tables' in d:
            o.check_sample_tables = d['check_sample_tables']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'description' in d:
            o.description = d['description']
        if 'domain_account' in d:
            o.domain_account = d['domain_account']
        if 'org_info' in d:
            o.org_info = d['org_info']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'review_history' in d:
            o.review_history = d['review_history']
        return o


