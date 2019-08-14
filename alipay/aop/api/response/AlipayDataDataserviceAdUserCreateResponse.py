#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdUserCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdUserCreateResponse, self).__init__()
        self._principal_id = None
        self._user_id = None

    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdUserCreateResponse, self).parse_response_content(response_content)
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
