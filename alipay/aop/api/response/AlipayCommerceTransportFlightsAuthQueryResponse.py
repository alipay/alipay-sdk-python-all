#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportFlightsAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportFlightsAuthQueryResponse, self).__init__()
        self._auth_status = None
        self._out_biz_no = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportFlightsAuthQueryResponse, self).parse_response_content(response_content)
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
