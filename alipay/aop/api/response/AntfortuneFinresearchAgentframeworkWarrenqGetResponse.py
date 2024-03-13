#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneFinresearchAgentframeworkWarrenqGetResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchAgentframeworkWarrenqGetResponse, self).__init__()
        self._result = None
        self._state = None
        self._steps = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        self._steps = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchAgentframeworkWarrenqGetResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'state' in response:
            self.state = response['state']
        if 'steps' in response:
            self.steps = response['steps']
