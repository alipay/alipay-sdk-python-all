#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KyaAgentInfo(object):

    def __init__(self):
        self._agent_id = None
        self._agent_status = None
        self._audit_status = None
        self._carrier = None
        self._cert_status = None
        self._logo = None
        self._name = None
        self._platform = None
        self._sub_name = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_status(self):
        return self._agent_status

    @agent_status.setter
    def agent_status(self, value):
        self._agent_status = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def carrier(self):
        return self._carrier

    @carrier.setter
    def carrier(self, value):
        self._carrier = value
    @property
    def cert_status(self):
        return self._cert_status

    @cert_status.setter
    def cert_status(self, value):
        self._cert_status = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def sub_name(self):
        return self._sub_name

    @sub_name.setter
    def sub_name(self, value):
        self._sub_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_status:
            if hasattr(self.agent_status, 'to_alipay_dict'):
                params['agent_status'] = self.agent_status.to_alipay_dict()
            else:
                params['agent_status'] = self.agent_status
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.carrier:
            if hasattr(self.carrier, 'to_alipay_dict'):
                params['carrier'] = self.carrier.to_alipay_dict()
            else:
                params['carrier'] = self.carrier
        if self.cert_status:
            if hasattr(self.cert_status, 'to_alipay_dict'):
                params['cert_status'] = self.cert_status.to_alipay_dict()
            else:
                params['cert_status'] = self.cert_status
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.sub_name:
            if hasattr(self.sub_name, 'to_alipay_dict'):
                params['sub_name'] = self.sub_name.to_alipay_dict()
            else:
                params['sub_name'] = self.sub_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KyaAgentInfo()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_status' in d:
            o.agent_status = d['agent_status']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'carrier' in d:
            o.carrier = d['carrier']
        if 'cert_status' in d:
            o.cert_status = d['cert_status']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'platform' in d:
            o.platform = d['platform']
        if 'sub_name' in d:
            o.sub_name = d['sub_name']
        return o


