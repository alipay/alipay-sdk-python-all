#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketShopPublicBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketShopPublicBindResponse, self).__init__()
        self._error_binding_shop_ids = None
        self._total_error = None
        self._total_success = None

    @property
    def error_binding_shop_ids(self):
        return self._error_binding_shop_ids

    @error_binding_shop_ids.setter
    def error_binding_shop_ids(self, value):
        if isinstance(value, list):
            self._error_binding_shop_ids = list()
            for i in value:
                self._error_binding_shop_ids.append(i)
    @property
    def total_error(self):
        return self._total_error

    @total_error.setter
    def total_error(self, value):
        self._total_error = value
    @property
    def total_success(self):
        return self._total_success

    @total_success.setter
    def total_success(self, value):
        self._total_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketShopPublicBindResponse, self).parse_response_content(response_content)
        if 'error_binding_shop_ids' in response:
            self.error_binding_shop_ids = response['error_binding_shop_ids']
        if 'total_error' in response:
            self.total_error = response['total_error']
        if 'total_success' in response:
            self.total_success = response['total_success']
