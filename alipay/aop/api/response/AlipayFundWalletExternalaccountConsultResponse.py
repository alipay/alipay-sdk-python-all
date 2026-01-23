#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WalletExternalAccount import WalletExternalAccount


class AlipayFundWalletExternalaccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletExternalaccountConsultResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._total_items = None
        self._total_pages = None
        self._wallet_external_accounts = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def wallet_external_accounts(self):
        return self._wallet_external_accounts

    @wallet_external_accounts.setter
    def wallet_external_accounts(self, value):
        if isinstance(value, WalletExternalAccount):
            self._wallet_external_accounts = value
        else:
            self._wallet_external_accounts = WalletExternalAccount.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletExternalaccountConsultResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'wallet_external_accounts' in response:
            self.wallet_external_accounts = response['wallet_external_accounts']
