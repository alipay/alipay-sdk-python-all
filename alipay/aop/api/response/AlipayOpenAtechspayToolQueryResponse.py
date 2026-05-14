#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ToolDatas import ToolDatas


class AlipayOpenAtechspayToolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAtechspayToolQueryResponse, self).__init__()
        self._diagnosis_info = None
        self._env = None
        self._tool = None

    @property
    def diagnosis_info(self):
        return self._diagnosis_info

    @diagnosis_info.setter
    def diagnosis_info(self, value):
        if isinstance(value, ToolDatas):
            self._diagnosis_info = value
        else:
            self._diagnosis_info = ToolDatas.from_alipay_dict(value)
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, value):
        self._tool = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAtechspayToolQueryResponse, self).parse_response_content(response_content)
        if 'diagnosis_info' in response:
            self.diagnosis_info = response['diagnosis_info']
        if 'env' in response:
            self.env = response['env']
        if 'tool' in response:
            self.tool = response['tool']
