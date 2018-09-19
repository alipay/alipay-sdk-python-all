#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingVoucherCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingVoucherCreateResponse, self).__init__()
        self._activity_id = None
        self._voucher_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketingVoucherCreateResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
