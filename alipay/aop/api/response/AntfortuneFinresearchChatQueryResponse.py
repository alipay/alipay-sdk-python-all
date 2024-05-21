#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZXZMessageDetail import ZXZMessageDetail


class AntfortuneFinresearchChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchChatQueryResponse, self).__init__()
        self._data = None
        self._result = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, ZXZMessageDetail):
            self._data = value
        else:
            self._data = ZXZMessageDetail.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchChatQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'result' in response:
            self.result = response['result']
