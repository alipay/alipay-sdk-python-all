#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundAccountBookInfoDTO import FundAccountBookInfoDTO


class AlipayCommerceCommonAccountbookQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonAccountbookQueryResponse, self).__init__()
        self._account_book_id = None
        self._account_book_info = None
        self._available_amount = None
        self._card_no = None
        self._page_no = None
        self._page_size = None
        self._total_size = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def account_book_info(self):
        return self._account_book_info

    @account_book_info.setter
    def account_book_info(self, value):
        if isinstance(value, list):
            self._account_book_info = list()
            for i in value:
                if isinstance(i, FundAccountBookInfoDTO):
                    self._account_book_info.append(i)
                else:
                    self._account_book_info.append(FundAccountBookInfoDTO.from_alipay_dict(i))
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonAccountbookQueryResponse, self).parse_response_content(response_content)
        if 'account_book_id' in response:
            self.account_book_id = response['account_book_id']
        if 'account_book_info' in response:
            self.account_book_info = response['account_book_info']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
