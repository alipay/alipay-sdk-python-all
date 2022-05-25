#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthJobdataAddResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthJobdataAddResponse, self).__init__()
        self._acceptance_id = None
        self._sub_code = None
        self._sub_msg = None
        self._url = None

    @property
    def acceptance_id(self):
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, value):
        self._acceptance_id = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_msg(self):
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, value):
        self._sub_msg = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthJobdataAddResponse, self).parse_response_content(response_content)
        if 'acceptance_id' in response:
            self.acceptance_id = response['acceptance_id']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
        if 'url' in response:
            self.url = response['url']
