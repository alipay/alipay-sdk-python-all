#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionOrderfundtransferModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionOrderfundtransferModifyResponse, self).__init__()
        self._modify_status = None
        self._out_flow_id = None
        self._out_order_no = None

    @property
    def modify_status(self):
        return self._modify_status

    @modify_status.setter
    def modify_status(self, value):
        self._modify_status = value
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
        response = super(AlipayEbppIndustrySupervisionOrderfundtransferModifyResponse, self).parse_response_content(response_content)
        if 'modify_status' in response:
            self.modify_status = response['modify_status']
        if 'out_flow_id' in response:
            self.out_flow_id = response['out_flow_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
