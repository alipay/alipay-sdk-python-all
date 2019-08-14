#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativeDetail import CreativeDetail


class AlipayDataDataserviceAdCreativeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdCreativeQueryResponse, self).__init__()
        self._creative_detail = None

    @property
    def creative_detail(self):
        return self._creative_detail

    @creative_detail.setter
    def creative_detail(self, value):
        if isinstance(value, CreativeDetail):
            self._creative_detail = value
        else:
            self._creative_detail = CreativeDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdCreativeQueryResponse, self).parse_response_content(response_content)
        if 'creative_detail' in response:
            self.creative_detail = response['creative_detail']
