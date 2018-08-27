#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationCustomerCertifyInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerCertifyInitializeResponse, self).__init__()
        self._biz_id = None
        self._zim_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerCertifyInitializeResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'zim_id' in response:
            self.zim_id = response['zim_id']
