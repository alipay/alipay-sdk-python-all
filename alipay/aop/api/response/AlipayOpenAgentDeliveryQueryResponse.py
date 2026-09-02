#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentDeliveryQueryResponse, self).__init__()
        self._agent_id = None
        self._agent_version = None
        self._channel = None
        self._delivery_status = None
        self._reject_reason = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_version(self):
        return self._agent_version

    @agent_version.setter
    def agent_version(self, value):
        self._agent_version = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'agent_version' in response:
            self.agent_version = response['agent_version']
        if 'channel' in response:
            self.channel = response['channel']
        if 'delivery_status' in response:
            self.delivery_status = response['delivery_status']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
