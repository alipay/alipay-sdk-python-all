#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceHkmedicalSigninResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceHkmedicalSigninResponse, self).__init__()
        self._cert_no = None
        self._cert_type = None
        self._company_type = None
        self._name = None
        self._open_id = None
        self._policy_no = None
        self._user_id = None

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
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceHkmedicalSigninResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'company_type' in response:
            self.company_type = response['company_type']
        if 'name' in response:
            self.name = response['name']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
