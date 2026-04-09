#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementDelegationSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementDelegationSignResponse, self).__init__()
        self._ai_pay_agreement_no = None
        self._delegation_id = None
        self._external_delegation_id = None
        self._no_pwd_agreement_no = None

    @property
    def ai_pay_agreement_no(self):
        return self._ai_pay_agreement_no

    @ai_pay_agreement_no.setter
    def ai_pay_agreement_no(self, value):
        self._ai_pay_agreement_no = value
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def external_delegation_id(self):
        return self._external_delegation_id

    @external_delegation_id.setter
    def external_delegation_id(self, value):
        self._external_delegation_id = value
    @property
    def no_pwd_agreement_no(self):
        return self._no_pwd_agreement_no

    @no_pwd_agreement_no.setter
    def no_pwd_agreement_no(self, value):
        self._no_pwd_agreement_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementDelegationSignResponse, self).parse_response_content(response_content)
        if 'ai_pay_agreement_no' in response:
            self.ai_pay_agreement_no = response['ai_pay_agreement_no']
        if 'delegation_id' in response:
            self.delegation_id = response['delegation_id']
        if 'external_delegation_id' in response:
            self.external_delegation_id = response['external_delegation_id']
        if 'no_pwd_agreement_no' in response:
            self.no_pwd_agreement_no = response['no_pwd_agreement_no']
