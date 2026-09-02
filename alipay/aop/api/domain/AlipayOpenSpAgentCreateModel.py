#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpAgentCreateModel(object):

    def __init__(self):
        self._account = None
        self._agent_desc = None
        self._agent_logo = None
        self._agent_name = None
        self._business_license_code = None
        self._business_license_name = None
        self._create_type = None
        self._legal_person_name = None
        self._template_id = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def agent_desc(self):
        return self._agent_desc

    @agent_desc.setter
    def agent_desc(self, value):
        self._agent_desc = value
    @property
    def agent_logo(self):
        return self._agent_logo

    @agent_logo.setter
    def agent_logo(self, value):
        self._agent_logo = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def business_license_code(self):
        return self._business_license_code

    @business_license_code.setter
    def business_license_code(self, value):
        self._business_license_code = value
    @property
    def business_license_name(self):
        return self._business_license_name

    @business_license_name.setter
    def business_license_name(self, value):
        self._business_license_name = value
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.agent_desc:
            if hasattr(self.agent_desc, 'to_alipay_dict'):
                params['agent_desc'] = self.agent_desc.to_alipay_dict()
            else:
                params['agent_desc'] = self.agent_desc
        if self.agent_logo:
            if hasattr(self.agent_logo, 'to_alipay_dict'):
                params['agent_logo'] = self.agent_logo.to_alipay_dict()
            else:
                params['agent_logo'] = self.agent_logo
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.business_license_code:
            if hasattr(self.business_license_code, 'to_alipay_dict'):
                params['business_license_code'] = self.business_license_code.to_alipay_dict()
            else:
                params['business_license_code'] = self.business_license_code
        if self.business_license_name:
            if hasattr(self.business_license_name, 'to_alipay_dict'):
                params['business_license_name'] = self.business_license_name.to_alipay_dict()
            else:
                params['business_license_name'] = self.business_license_name
        if self.create_type:
            if hasattr(self.create_type, 'to_alipay_dict'):
                params['create_type'] = self.create_type.to_alipay_dict()
            else:
                params['create_type'] = self.create_type
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpAgentCreateModel()
        if 'account' in d:
            o.account = d['account']
        if 'agent_desc' in d:
            o.agent_desc = d['agent_desc']
        if 'agent_logo' in d:
            o.agent_logo = d['agent_logo']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'business_license_code' in d:
            o.business_license_code = d['business_license_code']
        if 'business_license_name' in d:
            o.business_license_name = d['business_license_name']
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


