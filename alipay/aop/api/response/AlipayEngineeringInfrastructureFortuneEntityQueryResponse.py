#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FortuneEntityDTO import FortuneEntityDTO


class AlipayEngineeringInfrastructureFortuneEntityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEngineeringInfrastructureFortuneEntityQueryResponse, self).__init__()
        self._content = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, FortuneEntityDTO):
            self._content = value
        else:
            self._content = FortuneEntityDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEngineeringInfrastructureFortuneEntityQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
