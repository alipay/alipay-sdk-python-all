#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseTokenValidateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseTokenValidateQueryResponse, self).__init__()
        self._id_card_auth_status = None
        self._last_name = None
        self._passed_certificate_levels = None
        self._token_auth_status = None

    @property
    def id_card_auth_status(self):
        return self._id_card_auth_status

    @id_card_auth_status.setter
    def id_card_auth_status(self, value):
        self._id_card_auth_status = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def passed_certificate_levels(self):
        return self._passed_certificate_levels

    @passed_certificate_levels.setter
    def passed_certificate_levels(self, value):
        if isinstance(value, list):
            self._passed_certificate_levels = list()
            for i in value:
                self._passed_certificate_levels.append(i)
    @property
    def token_auth_status(self):
        return self._token_auth_status

    @token_auth_status.setter
    def token_auth_status(self, value):
        self._token_auth_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseTokenValidateQueryResponse, self).parse_response_content(response_content)
        if 'id_card_auth_status' in response:
            self.id_card_auth_status = response['id_card_auth_status']
        if 'last_name' in response:
            self.last_name = response['last_name']
        if 'passed_certificate_levels' in response:
            self.passed_certificate_levels = response['passed_certificate_levels']
        if 'token_auth_status' in response:
            self.token_auth_status = response['token_auth_status']
