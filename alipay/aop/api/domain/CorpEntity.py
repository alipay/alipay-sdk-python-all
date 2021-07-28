#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorpEntity(object):

    def __init__(self):
        self._agent_cert_name = None
        self._agent_cert_no = None
        self._alipay_account = None
        self._corp_code = None
        self._corp_name = None
        self._corp_type = None
        self._legal_cert_name = None
        self._legal_cert_no = None
        self._notify_email = None
        self._notify_name = None
        self._user_id = None

    @property
    def agent_cert_name(self):
        return self._agent_cert_name

    @agent_cert_name.setter
    def agent_cert_name(self, value):
        self._agent_cert_name = value
    @property
    def agent_cert_no(self):
        return self._agent_cert_no

    @agent_cert_no.setter
    def agent_cert_no(self, value):
        self._agent_cert_no = value
    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def corp_code(self):
        return self._corp_code

    @corp_code.setter
    def corp_code(self, value):
        self._corp_code = value
    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def corp_type(self):
        return self._corp_type

    @corp_type.setter
    def corp_type(self, value):
        self._corp_type = value
    @property
    def legal_cert_name(self):
        return self._legal_cert_name

    @legal_cert_name.setter
    def legal_cert_name(self, value):
        self._legal_cert_name = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def notify_email(self):
        return self._notify_email

    @notify_email.setter
    def notify_email(self, value):
        self._notify_email = value
    @property
    def notify_name(self):
        return self._notify_name

    @notify_name.setter
    def notify_name(self, value):
        self._notify_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_cert_name:
            if hasattr(self.agent_cert_name, 'to_alipay_dict'):
                params['agent_cert_name'] = self.agent_cert_name.to_alipay_dict()
            else:
                params['agent_cert_name'] = self.agent_cert_name
        if self.agent_cert_no:
            if hasattr(self.agent_cert_no, 'to_alipay_dict'):
                params['agent_cert_no'] = self.agent_cert_no.to_alipay_dict()
            else:
                params['agent_cert_no'] = self.agent_cert_no
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.corp_code:
            if hasattr(self.corp_code, 'to_alipay_dict'):
                params['corp_code'] = self.corp_code.to_alipay_dict()
            else:
                params['corp_code'] = self.corp_code
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.corp_type:
            if hasattr(self.corp_type, 'to_alipay_dict'):
                params['corp_type'] = self.corp_type.to_alipay_dict()
            else:
                params['corp_type'] = self.corp_type
        if self.legal_cert_name:
            if hasattr(self.legal_cert_name, 'to_alipay_dict'):
                params['legal_cert_name'] = self.legal_cert_name.to_alipay_dict()
            else:
                params['legal_cert_name'] = self.legal_cert_name
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.notify_email:
            if hasattr(self.notify_email, 'to_alipay_dict'):
                params['notify_email'] = self.notify_email.to_alipay_dict()
            else:
                params['notify_email'] = self.notify_email
        if self.notify_name:
            if hasattr(self.notify_name, 'to_alipay_dict'):
                params['notify_name'] = self.notify_name.to_alipay_dict()
            else:
                params['notify_name'] = self.notify_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpEntity()
        if 'agent_cert_name' in d:
            o.agent_cert_name = d['agent_cert_name']
        if 'agent_cert_no' in d:
            o.agent_cert_no = d['agent_cert_no']
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'corp_code' in d:
            o.corp_code = d['corp_code']
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'corp_type' in d:
            o.corp_type = d['corp_type']
        if 'legal_cert_name' in d:
            o.legal_cert_name = d['legal_cert_name']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'notify_email' in d:
            o.notify_email = d['notify_email']
        if 'notify_name' in d:
            o.notify_name = d['notify_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


