#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIcontrolVisitordispatchSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIcontrolVisitordispatchSubmitResponse, self).__init__()
        self._order_id = None
        self._order_position = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_position(self):
        return self._order_position

    @order_position.setter
    def order_position(self, value):
        self._order_position = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIcontrolVisitordispatchSubmitResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_position' in response:
            self.order_position = response['order_position']
