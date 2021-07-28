#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransEntrustCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransEntrustCloseResponse, self).__init__()
        self._entrust_order_id = None
        self._out_biz_no = None
        self._status = None

    @property
    def entrust_order_id(self):
        return self._entrust_order_id

    @entrust_order_id.setter
    def entrust_order_id(self, value):
        self._entrust_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransEntrustCloseResponse, self).parse_response_content(response_content)
        if 'entrust_order_id' in response:
            self.entrust_order_id = response['entrust_order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
