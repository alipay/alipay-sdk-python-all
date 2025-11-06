#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceUserskipQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceUserskipQueryResponse, self).__init__()
        self._open_id = None
        self._skip_url = None
        self._user_id = None
        self._user_token = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def skip_url(self):
        return self._skip_url

    @skip_url.setter
    def skip_url(self, value):
        self._skip_url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceUserskipQueryResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'skip_url' in response:
            self.skip_url = response['skip_url']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_token' in response:
            self.user_token = response['user_token']
