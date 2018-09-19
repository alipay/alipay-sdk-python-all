#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationUserWebQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationUserWebQueryResponse, self).__init__()
        self._extern_info = None

    @property
    def extern_info(self):
        return self._extern_info

    @extern_info.setter
    def extern_info(self, value):
        self._extern_info = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationUserWebQueryResponse, self).parse_response_content(response_content)
        if 'extern_info' in response:
            self.extern_info = response['extern_info']
