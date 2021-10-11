#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountbookNotifySubscribeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountbookNotifySubscribeResponse, self).__init__()
        self._account_book_id = None
        self._code = None
        self._msg = None
        self._subscribe_status = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def subscribe_status(self):
        return self._subscribe_status

    @subscribe_status.setter
    def subscribe_status(self, value):
        self._subscribe_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountbookNotifySubscribeResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'subscribe_status' in response:
            self.subscribe_status = response['subscribe_status']
