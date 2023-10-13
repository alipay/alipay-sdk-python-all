#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiAuthAmountInfoDTO import OpenApiAuthAmountInfoDTO


class AlipayBossBaseAntauthorizeMultiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseAntauthorizeMultiQueryResponse, self).__init__()
        self._auth_amount_info = None

    @property
    def auth_amount_info(self):
        return self._auth_amount_info

    @auth_amount_info.setter
    def auth_amount_info(self, value):
        if isinstance(value, OpenApiAuthAmountInfoDTO):
            self._auth_amount_info = value
        else:
            self._auth_amount_info = OpenApiAuthAmountInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseAntauthorizeMultiQueryResponse, self).parse_response_content(response_content)
        if 'auth_amount_info' in response:
            self.auth_amount_info = response['auth_amount_info']
