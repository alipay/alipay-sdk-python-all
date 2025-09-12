#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgentOperationAuthDetail import AgentOperationAuthDetail


class AlipayOpenSpInteopOpauthCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopOpauthCreateResponse, self).__init__()
        self._agent_operation_auth_details = None

    @property
    def agent_operation_auth_details(self):
        return self._agent_operation_auth_details

    @agent_operation_auth_details.setter
    def agent_operation_auth_details(self, value):
        if isinstance(value, list):
            self._agent_operation_auth_details = list()
            for i in value:
                if isinstance(i, AgentOperationAuthDetail):
                    self._agent_operation_auth_details.append(i)
                else:
                    self._agent_operation_auth_details.append(AgentOperationAuthDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopOpauthCreateResponse, self).parse_response_content(response_content)
        if 'agent_operation_auth_details' in response:
            self.agent_operation_auth_details = response['agent_operation_auth_details']
