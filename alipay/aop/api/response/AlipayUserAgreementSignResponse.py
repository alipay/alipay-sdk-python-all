#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementSignResponse, self).__init__()
        self._agreement_no = None
        self._alipay_logon_id = None
        self._alipay_user_id = None
        self._apply_token = None
        self._external_logon_id = None
        self._forex_eligible = None

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
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def apply_token(self):
        return self._apply_token

    @apply_token.setter
    def apply_token(self, value):
        self._apply_token = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def forex_eligible(self):
        return self._forex_eligible

    @forex_eligible.setter
    def forex_eligible(self, value):
        self._forex_eligible = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementSignResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'apply_token' in response:
            self.apply_token = response['apply_token']
        if 'external_logon_id' in response:
            self.external_logon_id = response['external_logon_id']
        if 'forex_eligible' in response:
            self.forex_eligible = response['forex_eligible']
