#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResponseMsg import ResponseMsg


class TechriskRiskaiOpsgptTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskRiskaiOpsgptTaskQueryResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, ResponseMsg):
            self._response = value
        else:
            self._response = ResponseMsg.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(TechriskRiskaiOpsgptTaskQueryResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
