#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAlixiaohaoQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAlixiaohaoQueryResponse, self).__init__()
        self._is_alixiaohao = None

    @property
    def is_alixiaohao(self):
        return self._is_alixiaohao

    @is_alixiaohao.setter
    def is_alixiaohao(self, value):
        self._is_alixiaohao = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAlixiaohaoQueryResponse, self).parse_response_content(response_content)
        if 'is_alixiaohao' in response:
            self.is_alixiaohao = response['is_alixiaohao']
