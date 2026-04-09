#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreateTextParamsResponse import CreateTextParamsResponse


class AnttechOceanbaseObglobalBailingualCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalBailingualCreateResponse, self).__init__()
        self._create_text_params_response = None

    @property
    def create_text_params_response(self):
        return self._create_text_params_response

    @create_text_params_response.setter
    def create_text_params_response(self, value):
        if isinstance(value, CreateTextParamsResponse):
            self._create_text_params_response = value
        else:
            self._create_text_params_response = CreateTextParamsResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalBailingualCreateResponse, self).parse_response_content(response_content)
        if 'create_text_params_response' in response:
            self.create_text_params_response = response['create_text_params_response']
