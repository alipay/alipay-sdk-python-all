#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RemoveTagResponse import RemoveTagResponse


class AntMerchantExpandScodeEledeUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandScodeEledeUnsignResponse, self).__init__()
        self._remove_tag_response = None

    @property
    def remove_tag_response(self):
        return self._remove_tag_response

    @remove_tag_response.setter
    def remove_tag_response(self, value):
        if isinstance(value, RemoveTagResponse):
            self._remove_tag_response = value
        else:
            self._remove_tag_response = RemoveTagResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandScodeEledeUnsignResponse, self).parse_response_content(response_content)
        if 'remove_tag_response' in response:
            self.remove_tag_response = response['remove_tag_response']
