#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationPointClearResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationPointClearResponse, self).__init__()
        self._order_id = None
        self._real_point = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def real_point(self):
        return self._real_point

    @real_point.setter
    def real_point(self, value):
        self._real_point = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationPointClearResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'real_point' in response:
            self.real_point = response['real_point']
