#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcChannelinvoiceMerchantopenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcChannelinvoiceMerchantopenGetResponse, self).__init__()
        self._company_name = None
        self._company_tax_no = None
        self._open_fail_reason = None
        self._open_status = None
        self._out_channel_merchant_id = None
        self._out_channel_merchant_name = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_tax_no(self):
        return self._company_tax_no

    @company_tax_no.setter
    def company_tax_no(self, value):
        self._company_tax_no = value
    @property
    def open_fail_reason(self):
        return self._open_fail_reason

    @open_fail_reason.setter
    def open_fail_reason(self, value):
        self._open_fail_reason = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def out_channel_merchant_id(self):
        return self._out_channel_merchant_id

    @out_channel_merchant_id.setter
    def out_channel_merchant_id(self, value):
        self._out_channel_merchant_id = value
    @property
    def out_channel_merchant_name(self):
        return self._out_channel_merchant_name

    @out_channel_merchant_name.setter
    def out_channel_merchant_name(self, value):
        self._out_channel_merchant_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcChannelinvoiceMerchantopenGetResponse, self).parse_response_content(response_content)
        if 'company_name' in response:
            self.company_name = response['company_name']
        if 'company_tax_no' in response:
            self.company_tax_no = response['company_tax_no']
        if 'open_fail_reason' in response:
            self.open_fail_reason = response['open_fail_reason']
        if 'open_status' in response:
            self.open_status = response['open_status']
        if 'out_channel_merchant_id' in response:
            self.out_channel_merchant_id = response['out_channel_merchant_id']
        if 'out_channel_merchant_name' in response:
            self.out_channel_merchant_name = response['out_channel_merchant_name']
