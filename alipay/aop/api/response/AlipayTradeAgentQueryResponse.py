#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeAgentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeAgentQueryResponse, self).__init__()
        self._agent_id = None
        self._operation = None
        self._out_request_no = None
        self._reject_reason = None
        self._status = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeAgentQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'operation' in response:
            self.operation = response['operation']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'status' in response:
            self.status = response['status']
