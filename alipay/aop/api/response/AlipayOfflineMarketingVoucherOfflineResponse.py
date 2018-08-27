#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingVoucherOfflineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingVoucherOfflineResponse, self).__init__()
        self._voucher_id = None
        self._voucher_status = None

    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketingVoucherOfflineResponse, self).parse_response_content(response_content)
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
        if 'voucher_status' in response:
            self.voucher_status = response['voucher_status']
