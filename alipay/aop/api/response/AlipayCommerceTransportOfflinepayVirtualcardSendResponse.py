#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportOfflinepayVirtualcardSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOfflinepayVirtualcardSendResponse, self).__init__()
        self._card_no = None
        self._card_schema = None
        self._card_type = None
        self._error_message = None
        self._sub_error_code = None
        self._user_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_schema(self):
        return self._card_schema

    @card_schema.setter
    def card_schema(self, value):
        self._card_schema = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def sub_error_code(self):
        return self._sub_error_code

    @sub_error_code.setter
    def sub_error_code(self, value):
        self._sub_error_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOfflinepayVirtualcardSendResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'card_schema' in response:
            self.card_schema = response['card_schema']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'sub_error_code' in response:
            self.sub_error_code = response['sub_error_code']
        if 'user_id' in response:
            self.user_id = response['user_id']
