#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementAgentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementAgentQueryResponse, self).__init__()
        self._agreement_no = None
        self._alipay_logon_id = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._external_user_id = None
        self._invalid_time = None
        self._status = None
        self._valid_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementAgentQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'external_agreement_no' in response:
            self.external_agreement_no = response['external_agreement_no']
        if 'external_logon_id' in response:
            self.external_logon_id = response['external_logon_id']
        if 'external_user_id' in response:
            self.external_user_id = response['external_user_id']
        if 'invalid_time' in response:
            self.invalid_time = response['invalid_time']
        if 'status' in response:
            self.status = response['status']
        if 'valid_time' in response:
            self.valid_time = response['valid_time']
