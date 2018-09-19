#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherSendResponse, self).__init__()
        self._user_id = None
        self._voucher_id = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherSendResponse, self).parse_response_content(response_content)
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
