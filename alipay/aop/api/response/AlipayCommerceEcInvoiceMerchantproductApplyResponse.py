#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcInvoiceMerchantproductApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcInvoiceMerchantproductApplyResponse, self).__init__()
        self._apply_id = None
        self._flow_status = None
        self._open_page_url = None
        self._out_apply_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def flow_status(self):
        return self._flow_status

    @flow_status.setter
    def flow_status(self, value):
        self._flow_status = value
    @property
    def open_page_url(self):
        return self._open_page_url

    @open_page_url.setter
    def open_page_url(self, value):
        self._open_page_url = value
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcInvoiceMerchantproductApplyResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'flow_status' in response:
            self.flow_status = response['flow_status']
        if 'open_page_url' in response:
            self.open_page_url = response['open_page_url']
        if 'out_apply_id' in response:
            self.out_apply_id = response['out_apply_id']
