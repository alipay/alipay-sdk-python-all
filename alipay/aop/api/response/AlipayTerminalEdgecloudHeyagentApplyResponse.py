#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTerminalEdgecloudHeyagentApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTerminalEdgecloudHeyagentApplyResponse, self).__init__()
        self._agent_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTerminalEdgecloudHeyagentApplyResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
