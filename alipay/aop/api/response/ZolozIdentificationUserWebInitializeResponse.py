#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationUserWebInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationUserWebInitializeResponse, self).__init__()
        self._extern_info = None
        self._zim_id = None

    @property
    def extern_info(self):
        return self._extern_info

    @extern_info.setter
    def extern_info(self, value):
        self._extern_info = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationUserWebInitializeResponse, self).parse_response_content(response_content)
        if 'extern_info' in response:
            self.extern_info = response['extern_info']
        if 'zim_id' in response:
            self.zim_id = response['zim_id']
