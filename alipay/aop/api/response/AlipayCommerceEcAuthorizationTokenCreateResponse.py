#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenAccessTokenDTO import OpenAccessTokenDTO


class AlipayCommerceEcAuthorizationTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAuthorizationTokenCreateResponse, self).__init__()
        self._open_access_token_dto = None

    @property
    def open_access_token_dto(self):
        return self._open_access_token_dto

    @open_access_token_dto.setter
    def open_access_token_dto(self, value):
        if isinstance(value, OpenAccessTokenDTO):
            self._open_access_token_dto = value
        else:
            self._open_access_token_dto = OpenAccessTokenDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAuthorizationTokenCreateResponse, self).parse_response_content(response_content)
        if 'open_access_token_dto' in response:
            self.open_access_token_dto = response['open_access_token_dto']
