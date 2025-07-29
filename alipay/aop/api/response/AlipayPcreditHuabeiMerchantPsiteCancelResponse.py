#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiMerchantPsiteCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiMerchantPsiteCancelResponse, self).__init__()
        self._has_cancel = None
        self._out_request_no = None

    @property
    def has_cancel(self):
        return self._has_cancel

    @has_cancel.setter
    def has_cancel(self, value):
        self._has_cancel = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiMerchantPsiteCancelResponse, self).parse_response_content(response_content)
        if 'has_cancel' in response:
            self.has_cancel = response['has_cancel']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
