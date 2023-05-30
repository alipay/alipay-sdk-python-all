#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HardeningTaskResponse import HardeningTaskResponse


class AlipaySecurityProdAshieldHardeningtaskprocessGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAshieldHardeningtaskprocessGetResponse, self).__init__()
        self._request_id = None
        self._res_data = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def res_data(self):
        return self._res_data

    @res_data.setter
    def res_data(self, value):
        if isinstance(value, HardeningTaskResponse):
            self._res_data = value
        else:
            self._res_data = HardeningTaskResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAshieldHardeningtaskprocessGetResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'res_data' in response:
            self.res_data = response['res_data']
