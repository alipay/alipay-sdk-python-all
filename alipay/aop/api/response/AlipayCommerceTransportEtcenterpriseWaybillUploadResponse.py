#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcenterpriseWaybillUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseWaybillUploadResponse, self).__init__()
        self._biz_code = None
        self._biz_id = None
        self._biz_msg = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseWaybillUploadResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
