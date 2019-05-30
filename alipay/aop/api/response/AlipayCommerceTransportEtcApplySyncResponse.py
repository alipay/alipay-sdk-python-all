#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcApplySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcApplySyncResponse, self).__init__()
        self._order_id = None
        self._out_biz_no = None
        self._sync_result = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sync_result(self):
        return self._sync_result

    @sync_result.setter
    def sync_result(self, value):
        self._sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcApplySyncResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'sync_result' in response:
            self.sync_result = response['sync_result']
