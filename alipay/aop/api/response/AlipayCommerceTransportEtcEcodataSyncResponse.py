#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcEcodataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcEcodataSyncResponse, self).__init__()
        self._alipay_biz_no = None
        self._sync_result = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value
    @property
    def sync_result(self):
        return self._sync_result

    @sync_result.setter
    def sync_result(self, value):
        self._sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcEcodataSyncResponse, self).parse_response_content(response_content)
        if 'alipay_biz_no' in response:
            self.alipay_biz_no = response['alipay_biz_no']
        if 'sync_result' in response:
            self.sync_result = response['sync_result']
