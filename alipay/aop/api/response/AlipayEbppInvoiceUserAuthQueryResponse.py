#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceUserAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceUserAuthQueryResponse, self).__init__()
        self._has_authorized = None
        self._open_id = None
        self._protocol_url = None
        self._user_id = None

    @property
    def has_authorized(self):
        return self._has_authorized

    @has_authorized.setter
    def has_authorized(self, value):
        self._has_authorized = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def protocol_url(self):
        return self._protocol_url

    @protocol_url.setter
    def protocol_url(self, value):
        self._protocol_url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceUserAuthQueryResponse, self).parse_response_content(response_content)
        if 'has_authorized' in response:
            self.has_authorized = response['has_authorized']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'protocol_url' in response:
            self.protocol_url = response['protocol_url']
        if 'user_id' in response:
            self.user_id = response['user_id']
