#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationCustomerCertifyzhubInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerCertifyzhubInitializeResponse, self).__init__()
        self._biz_id = None
        self._zim_code = None
        self._zim_id = None
        self._zim_msg = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def zim_code(self):
        return self._zim_code

    @zim_code.setter
    def zim_code(self, value):
        self._zim_code = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value
    @property
    def zim_msg(self):
        return self._zim_msg

    @zim_msg.setter
    def zim_msg(self, value):
        self._zim_msg = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerCertifyzhubInitializeResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'zim_code' in response:
            self.zim_code = response['zim_code']
        if 'zim_id' in response:
            self.zim_id = response['zim_id']
        if 'zim_msg' in response:
            self.zim_msg = response['zim_msg']
