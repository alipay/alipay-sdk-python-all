#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoAutoaftermarketOutorderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoaftermarketOutorderSyncResponse, self).__init__()
        self._ant_order_no = None

    @property
    def ant_order_no(self):
        return self._ant_order_no

    @ant_order_no.setter
    def ant_order_no(self, value):
        self._ant_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoaftermarketOutorderSyncResponse, self).parse_response_content(response_content)
        if 'ant_order_no' in response:
            self.ant_order_no = response['ant_order_no']
