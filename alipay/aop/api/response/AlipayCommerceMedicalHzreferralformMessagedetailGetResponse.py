#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHzreferralformMessagedetailGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHzreferralformMessagedetailGetResponse, self).__init__()
        self._agent_url = None
        self._cert_no = None
        self._name = None
        self._phone_no = None

    @property
    def agent_url(self):
        return self._agent_url

    @agent_url.setter
    def agent_url(self, value):
        self._agent_url = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHzreferralformMessagedetailGetResponse, self).parse_response_content(response_content)
        if 'agent_url' in response:
            self.agent_url = response['agent_url']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'name' in response:
            self.name = response['name']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
