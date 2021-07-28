#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtCardInfo import ExtCardInfo


class AlipayFundAccountbookCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountbookCreateResponse, self).__init__()
        self._account_book_id = None
        self._ext_card_info = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def ext_card_info(self):
        return self._ext_card_info

    @ext_card_info.setter
    def ext_card_info(self, value):
        if isinstance(value, ExtCardInfo):
            self._ext_card_info = value
        else:
            self._ext_card_info = ExtCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountbookCreateResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
        if 'ext_card_info' in response:
            self.ext_card_info = response['ext_card_info']
