#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionOrderCreateResponse, self).__init__()
        self._alipay_order_detail_url = None
        self._order_status = None
        self._out_order_no = None

    @property
    def alipay_order_detail_url(self):
        return self._alipay_order_detail_url

    @alipay_order_detail_url.setter
    def alipay_order_detail_url(self, value):
        self._alipay_order_detail_url = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionOrderCreateResponse, self).parse_response_content(response_content)
        if 'alipay_order_detail_url' in response:
            self.alipay_order_detail_url = response['alipay_order_detail_url']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
