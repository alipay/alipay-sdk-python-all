#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistPromoVoucherNotifyResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistPromoVoucherNotifyResponse, self).__init__()
        self._inst_voucher_id = None
        self._request_id = None
        self._retry = None
        self._voucher_id = None

    @property
    def inst_voucher_id(self):
        return self._inst_voucher_id

    @inst_voucher_id.setter
    def inst_voucher_id(self, value):
        self._inst_voucher_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistPromoVoucherNotifyResponse, self).parse_response_content(response_content)
        if 'inst_voucher_id' in response:
            self.inst_voucher_id = response['inst_voucher_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'retry' in response:
            self.retry = response['retry']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
