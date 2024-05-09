#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WalletOperationDetails import WalletOperationDetails


class AlipayCloudFundWalletOperationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundWalletOperationQueryResponse, self).__init__()
        self._current_page = None
        self._total_items = None
        self._total_pages = None
        self._wallet_operations = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
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
    def wallet_operations(self):
        return self._wallet_operations

    @wallet_operations.setter
    def wallet_operations(self, value):
        if isinstance(value, WalletOperationDetails):
            self._wallet_operations = value
        else:
            self._wallet_operations = WalletOperationDetails.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudFundWalletOperationQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'wallet_operations' in response:
            self.wallet_operations = response['wallet_operations']
