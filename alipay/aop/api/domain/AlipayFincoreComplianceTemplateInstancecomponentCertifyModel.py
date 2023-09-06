#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateInstancecomponentCertifyModel(object):

    def __init__(self):
        self._component_code = None
        self._domain_name = None
        self._nick_name = None
        self._secret = None
        self._source_system_id = None
        self._tenant = None
        self._work_no = None

    @property
    def component_code(self):
        return self._component_code

    @component_code.setter
    def component_code(self, value):
        self._component_code = value
    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        self._domain_name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.component_code:
            if hasattr(self.component_code, 'to_alipay_dict'):
                params['component_code'] = self.component_code.to_alipay_dict()
            else:
                params['component_code'] = self.component_code
        if self.domain_name:
            if hasattr(self.domain_name, 'to_alipay_dict'):
                params['domain_name'] = self.domain_name.to_alipay_dict()
            else:
                params['domain_name'] = self.domain_name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.secret:
            if hasattr(self.secret, 'to_alipay_dict'):
                params['secret'] = self.secret.to_alipay_dict()
            else:
                params['secret'] = self.secret
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceTemplateInstancecomponentCertifyModel()
        if 'component_code' in d:
            o.component_code = d['component_code']
        if 'domain_name' in d:
            o.domain_name = d['domain_name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'secret' in d:
            o.secret = d['secret']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


