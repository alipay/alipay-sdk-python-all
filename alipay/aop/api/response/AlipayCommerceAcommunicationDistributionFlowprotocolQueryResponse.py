#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FlowProtocol import FlowProtocol


class AlipayCommerceAcommunicationDistributionFlowprotocolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionFlowprotocolQueryResponse, self).__init__()
        self._protocol_list = None
        self._protocol_sequence_id = None

    @property
    def protocol_list(self):
        return self._protocol_list

    @protocol_list.setter
    def protocol_list(self, value):
        if isinstance(value, list):
            self._protocol_list = list()
            for i in value:
                if isinstance(i, FlowProtocol):
                    self._protocol_list.append(i)
                else:
                    self._protocol_list.append(FlowProtocol.from_alipay_dict(i))
    @property
    def protocol_sequence_id(self):
        return self._protocol_sequence_id

    @protocol_sequence_id.setter
    def protocol_sequence_id(self, value):
        self._protocol_sequence_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionFlowprotocolQueryResponse, self).parse_response_content(response_content)
        if 'protocol_list' in response:
            self.protocol_list = response['protocol_list']
        if 'protocol_sequence_id' in response:
            self.protocol_sequence_id = response['protocol_sequence_id']
