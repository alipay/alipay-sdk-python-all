#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionTransfermaterialSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionTransfermaterialSubmitResponse, self).__init__()
        self._biz_status = None
        self._out_flow_id = None
        self._out_order_no = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def out_flow_id(self):
        return self._out_flow_id

    @out_flow_id.setter
    def out_flow_id(self, value):
        self._out_flow_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionTransfermaterialSubmitResponse, self).parse_response_content(response_content)
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'out_flow_id' in response:
            self.out_flow_id = response['out_flow_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
