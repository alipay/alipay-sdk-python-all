#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransAppPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAppPayResponse, self).__init__()
        self._order_id = None
        self._out_biz_no = None
        self._pageRedirectionData = None
        self._status = None

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
    def pageRedirectionData(self):
        return self._pageRedirectionData

    @pageRedirectionData.setter
    def pageRedirectionData(self, value):
        self._pageRedirectionData = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAppPayResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'pageRedirectionData' in response:
            self.pageRedirectionData = response['pageRedirectionData']
        if 'status' in response:
            self.status = response['status']
