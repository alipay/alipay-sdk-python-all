#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AsyncSubmitTaskResponse import AsyncSubmitTaskResponse


class TechriskRiskaiOpsgptTaskasyncSubmitResponse(AlipayResponse):

    def __init__(self):
        super(TechriskRiskaiOpsgptTaskasyncSubmitResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, AsyncSubmitTaskResponse):
            self._response = value
        else:
            self._response = AsyncSubmitTaskResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(TechriskRiskaiOpsgptTaskasyncSubmitResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
