#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectBindQrcodecreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectBindQrcodecreateResponse, self).__init__()
        self._fail_reason = None
        self._has_apply = None
        self._order_id = None
        self._qr_code_url = None
        self._status = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def has_apply(self):
        return self._has_apply

    @has_apply.setter
    def has_apply(self, value):
        self._has_apply = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectBindQrcodecreateResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'has_apply' in response:
            self.has_apply = response['has_apply']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
        if 'status' in response:
            self.status = response['status']
