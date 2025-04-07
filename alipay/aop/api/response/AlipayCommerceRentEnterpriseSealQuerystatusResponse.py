#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentEnterpriseSealQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentEnterpriseSealQuerystatusResponse, self).__init__()
        self._biz_no = None
        self._http_file_url = None
        self._sign_flow_id = None
        self._status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def http_file_url(self):
        return self._http_file_url

    @http_file_url.setter
    def http_file_url(self, value):
        self._http_file_url = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentEnterpriseSealQuerystatusResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'http_file_url' in response:
            self.http_file_url = response['http_file_url']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
        if 'status' in response:
            self.status = response['status']
