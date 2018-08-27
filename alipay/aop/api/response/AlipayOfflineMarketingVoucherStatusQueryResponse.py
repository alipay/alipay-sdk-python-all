#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingVoucherStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingVoucherStatusQueryResponse, self).__init__()
        self._ext_info = None
        self._voucher_id = None
        self._voucher_status = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
        response = super(AlipayOfflineMarketingVoucherStatusQueryResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
        if 'voucher_status' in response:
            self.voucher_status = response['voucher_status']
