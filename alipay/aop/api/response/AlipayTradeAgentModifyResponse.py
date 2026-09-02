#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeAgentModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeAgentModifyResponse, self).__init__()
        self._agent_id = None
        self._order_id = None
        self._status = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeAgentModifyResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'status' in response:
            self.status = response['status']
