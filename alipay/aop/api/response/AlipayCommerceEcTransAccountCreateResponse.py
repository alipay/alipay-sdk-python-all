#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TransInCardInfo import TransInCardInfo


class AlipayCommerceEcTransAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransAccountCreateResponse, self).__init__()
        self._account_book_id = None
        self._account_card_info = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def account_card_info(self):
        return self._account_card_info

    @account_card_info.setter
    def account_card_info(self, value):
        if isinstance(value, TransInCardInfo):
            self._account_card_info = value
        else:
            self._account_card_info = TransInCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTransAccountCreateResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
        if 'account_card_info' in response:
            self.account_card_info = response['account_card_info']
