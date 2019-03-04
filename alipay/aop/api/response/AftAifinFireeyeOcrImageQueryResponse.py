#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OcrIdentifyResult import OcrIdentifyResult


class AftAifinFireeyeOcrImageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AftAifinFireeyeOcrImageQueryResponse, self).__init__()
        self._content = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, OcrIdentifyResult):
            self._content = value
        else:
            self._content = OcrIdentifyResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AftAifinFireeyeOcrImageQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
