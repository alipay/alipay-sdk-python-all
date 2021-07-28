#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsDataAuthorizationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataAuthorizationQueryResponse, self).__init__()
        self._auth_agreement_url = None
        self._relation_to_insured = None

    @property
    def auth_agreement_url(self):
        return self._auth_agreement_url

    @auth_agreement_url.setter
    def auth_agreement_url(self, value):
        self._auth_agreement_url = value
    @property
    def relation_to_insured(self):
        return self._relation_to_insured

    @relation_to_insured.setter
    def relation_to_insured(self, value):
        self._relation_to_insured = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataAuthorizationQueryResponse, self).parse_response_content(response_content)
        if 'auth_agreement_url' in response:
            self.auth_agreement_url = response['auth_agreement_url']
        if 'relation_to_insured' in response:
            self.relation_to_insured = response['relation_to_insured']
