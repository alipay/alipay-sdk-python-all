#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserUnicomCardInfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUnicomCardInfoSyncResponse, self).__init__()
        self._card_sync_result = None
        self._phone_no = None
        self._user_id = None

    @property
    def card_sync_result(self):
        return self._card_sync_result

    @card_sync_result.setter
    def card_sync_result(self, value):
        self._card_sync_result = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUnicomCardInfoSyncResponse, self).parse_response_content(response_content)
        if 'card_sync_result' in response:
            self.card_sync_result = response['card_sync_result']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
