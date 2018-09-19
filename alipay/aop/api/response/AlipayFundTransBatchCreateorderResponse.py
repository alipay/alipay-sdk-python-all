#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransBatchCreateorderResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransBatchCreateorderResponse, self).__init__()
        self._biz_type = None
        self._ext_param = None
        self._transfer_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransBatchCreateorderResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'ext_param' in response:
            self.ext_param = response['ext_param']
        if 'transfer_no' in response:
            self.transfer_no = response['transfer_no']
