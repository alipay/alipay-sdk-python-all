#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTerminalEdgecloudHeyagentDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTerminalEdgecloudHeyagentDataQueryResponse, self).__init__()
        self._agent_id = None
        self._dom = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def dom(self):
        return self._dom

    @dom.setter
    def dom(self, value):
        self._dom = value

    def parse_response_content(self, response_content):
        response = super(AlipayTerminalEdgecloudHeyagentDataQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'dom' in response:
            self.dom = response['dom']
