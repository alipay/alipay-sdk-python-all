#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AuthInfoDTO import AuthInfoDTO
from alipay.aop.api.domain.ExtCardInfo import ExtCardInfo


class AlipayFundAccountbookQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountbookQueryResponse, self).__init__()
        self._account_book_id = None
        self._auth_info = None
        self._available_amount = None
        self._ext_card_info = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def auth_info(self):
        return self._auth_info

    @auth_info.setter
    def auth_info(self, value):
        if isinstance(value, AuthInfoDTO):
            self._auth_info = value
        else:
            self._auth_info = AuthInfoDTO.from_alipay_dict(value)
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
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
        response = super(AlipayFundAccountbookQueryResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
        if 'auth_info' in response:
            self.auth_info = response['auth_info']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'ext_card_info' in response:
            self.ext_card_info = response['ext_card_info']
