#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceTruspleAuthloginSubmitModel(object):

    def __init__(self):
        self._cert_no = None
        self._company_cert_no = None
        self._company_name = None
        self._inst_code = None
        self._login_id = None
        self._phone_no = None
        self._state = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTruspleAuthloginSubmitModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'state' in d:
            o.state = d['state']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


