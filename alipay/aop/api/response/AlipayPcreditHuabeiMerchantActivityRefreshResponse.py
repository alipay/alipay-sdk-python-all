#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiMerchantActivityRefreshResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiMerchantActivityRefreshResponse, self).__init__()
        self._aggr_id = None
        self._out_request_no = None

    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiMerchantActivityRefreshResponse, self).parse_response_content(response_content)
        if 'aggr_id' in response:
            self.aggr_id = response['aggr_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
