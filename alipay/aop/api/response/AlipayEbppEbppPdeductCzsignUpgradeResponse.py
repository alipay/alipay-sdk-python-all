#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppEbppPdeductCzsignUpgradeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEbppPdeductCzsignUpgradeResponse, self).__init__()
        self._error_message = None
        self._new_agreement_id = None
        self._success = None
        self._user_id = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def new_agreement_id(self):
        return self._new_agreement_id

    @new_agreement_id.setter
    def new_agreement_id(self, value):
        self._new_agreement_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppEbppPdeductCzsignUpgradeResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'new_agreement_id' in response:
            self.new_agreement_id = response['new_agreement_id']
        if 'success' in response:
            self.success = response['success']
        if 'user_id' in response:
            self.user_id = response['user_id']
