#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddTagResponse import AddTagResponse


class AntMerchantExpandScodeEledeSignResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandScodeEledeSignResponse, self).__init__()
        self._add_tag_response = None

    @property
    def add_tag_response(self):
        return self._add_tag_response

    @add_tag_response.setter
    def add_tag_response(self, value):
        if isinstance(value, AddTagResponse):
            self._add_tag_response = value
        else:
            self._add_tag_response = AddTagResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandScodeEledeSignResponse, self).parse_response_content(response_content)
        if 'add_tag_response' in response:
            self.add_tag_response = response['add_tag_response']
