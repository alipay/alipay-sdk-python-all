#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoMallRenfundorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallRenfundorderCreateResponse, self).__init__()
        self._dispute_id = None
        self._dispute_status = None
        self._order_line_id = None

    @property
    def dispute_id(self):
        return self._dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self._dispute_id = value
    @property
    def dispute_status(self):
        return self._dispute_status

    @dispute_status.setter
    def dispute_status(self, value):
        self._dispute_status = value
    @property
    def order_line_id(self):
        return self._order_line_id

    @order_line_id.setter
    def order_line_id(self, value):
        self._order_line_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallRenfundorderCreateResponse, self).parse_response_content(response_content)
        if 'dispute_id' in response:
            self.dispute_id = response['dispute_id']
        if 'dispute_status' in response:
            self.dispute_status = response['dispute_status']
        if 'order_line_id' in response:
            self.order_line_id = response['order_line_id']
