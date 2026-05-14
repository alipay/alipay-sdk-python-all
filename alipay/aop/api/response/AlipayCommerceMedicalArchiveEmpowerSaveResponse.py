#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalArchiveEmpowerSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalArchiveEmpowerSaveResponse, self).__init__()
        self._access_token = None
        self._archives_member_url = None
        self._member_validate = None
        self._token_validity = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def archives_member_url(self):
        return self._archives_member_url

    @archives_member_url.setter
    def archives_member_url(self, value):
        self._archives_member_url = value
    @property
    def member_validate(self):
        return self._member_validate

    @member_validate.setter
    def member_validate(self, value):
        self._member_validate = value
    @property
    def token_validity(self):
        return self._token_validity

    @token_validity.setter
    def token_validity(self, value):
        self._token_validity = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalArchiveEmpowerSaveResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'archives_member_url' in response:
            self.archives_member_url = response['archives_member_url']
        if 'member_validate' in response:
            self.member_validate = response['member_validate']
        if 'token_validity' in response:
            self.token_validity = response['token_validity']
