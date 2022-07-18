#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdentityDTO(object):

    def __init__(self):
        self._agent = None
        self._agent_id = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._legal_person = None
        self._legal_person_id = None
        self._mobile_no = None
        self._user_type = None

    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, value):
        self._agent = value
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def legal_person(self):
        return self._legal_person

    @legal_person.setter
    def legal_person(self, value):
        self._legal_person = value
    @property
    def legal_person_id(self):
        return self._legal_person_id

    @legal_person_id.setter
    def legal_person_id(self, value):
        self._legal_person_id = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent:
            if hasattr(self.agent, 'to_alipay_dict'):
                params['agent'] = self.agent.to_alipay_dict()
            else:
                params['agent'] = self.agent
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.legal_person:
            if hasattr(self.legal_person, 'to_alipay_dict'):
                params['legal_person'] = self.legal_person.to_alipay_dict()
            else:
                params['legal_person'] = self.legal_person
        if self.legal_person_id:
            if hasattr(self.legal_person_id, 'to_alipay_dict'):
                params['legal_person_id'] = self.legal_person_id.to_alipay_dict()
            else:
                params['legal_person_id'] = self.legal_person_id
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdentityDTO()
        if 'agent' in d:
            o.agent = d['agent']
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'legal_person' in d:
            o.legal_person = d['legal_person']
        if 'legal_person_id' in d:
            o.legal_person_id = d['legal_person_id']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


