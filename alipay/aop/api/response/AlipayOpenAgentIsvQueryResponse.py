#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentIsvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentIsvQueryResponse, self).__init__()
        self._agent_app_id = None
        self._order_no = None
        self._out_order_no = None
        self._status = None

    @property
    def agent_app_id(self):
        return self._agent_app_id

    @agent_app_id.setter
    def agent_app_id(self, value):
        self._agent_app_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentIsvQueryResponse, self).parse_response_content(response_content)
        if 'agent_app_id' in response:
            self.agent_app_id = response['agent_app_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
