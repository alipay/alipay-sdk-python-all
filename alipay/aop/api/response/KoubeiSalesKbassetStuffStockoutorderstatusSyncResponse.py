#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiSalesKbassetStuffStockoutorderstatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffStockoutorderstatusSyncResponse, self).__init__()
        self._erp_order = None
        self._error_code = None
        self._error_desc = None
        self._success = None

    @property
    def erp_order(self):
        return self._erp_order

    @erp_order.setter
    def erp_order(self, value):
        self._erp_order = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffStockoutorderstatusSyncResponse, self).parse_response_content(response_content)
        if 'erp_order' in response:
            self.erp_order = response['erp_order']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_desc' in response:
            self.error_desc = response['error_desc']
        if 'success' in response:
            self.success = response['success']
