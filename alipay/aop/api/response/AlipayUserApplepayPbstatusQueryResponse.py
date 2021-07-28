#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiPassStatus import OpenApiPassStatus
from alipay.aop.api.domain.OpenApiResponseHeader import OpenApiResponseHeader


class AlipayUserApplepayPbstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserApplepayPbstatusQueryResponse, self).__init__()
        self._pass_status_list = None
        self._response_header = None
        self._state = None

    @property
    def pass_status_list(self):
        return self._pass_status_list

    @pass_status_list.setter
    def pass_status_list(self, value):
        if isinstance(value, OpenApiPassStatus):
            self._pass_status_list = value
        else:
            self._pass_status_list = OpenApiPassStatus.from_alipay_dict(value)
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, OpenApiResponseHeader):
            self._response_header = value
        else:
            self._response_header = OpenApiResponseHeader.from_alipay_dict(value)
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserApplepayPbstatusQueryResponse, self).parse_response_content(response_content)
        if 'pass_status_list' in response:
            self.pass_status_list = response['pass_status_list']
        if 'response_header' in response:
            self.response_header = response['response_header']
        if 'state' in response:
            self.state = response['state']
