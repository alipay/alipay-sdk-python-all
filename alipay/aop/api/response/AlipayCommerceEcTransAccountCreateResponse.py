#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTransAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransAccountCreateResponse, self).__init__()
        self._account_book_id = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTransAccountCreateResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
