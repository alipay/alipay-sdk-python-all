#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenDeleteCreativeResponse import OpenDeleteCreativeResponse


class AlipayDataDataserviceAdCreativeDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdCreativeDeleteResponse, self).__init__()
        self._open_delete_creative_response = None

    @property
    def open_delete_creative_response(self):
        return self._open_delete_creative_response

    @open_delete_creative_response.setter
    def open_delete_creative_response(self, value):
        if isinstance(value, OpenDeleteCreativeResponse):
            self._open_delete_creative_response = value
        else:
            self._open_delete_creative_response = OpenDeleteCreativeResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdCreativeDeleteResponse, self).parse_response_content(response_content)
        if 'open_delete_creative_response' in response:
            self.open_delete_creative_response = response['open_delete_creative_response']
