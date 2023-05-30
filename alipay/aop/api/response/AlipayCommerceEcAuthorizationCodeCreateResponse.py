#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenAccessCodeDTO import OpenAccessCodeDTO


class AlipayCommerceEcAuthorizationCodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAuthorizationCodeCreateResponse, self).__init__()
        self._open_access_code_dto = None

    @property
    def open_access_code_dto(self):
        return self._open_access_code_dto

    @open_access_code_dto.setter
    def open_access_code_dto(self, value):
        if isinstance(value, OpenAccessCodeDTO):
            self._open_access_code_dto = value
        else:
            self._open_access_code_dto = OpenAccessCodeDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAuthorizationCodeCreateResponse, self).parse_response_content(response_content)
        if 'open_access_code_dto' in response:
            self.open_access_code_dto = response['open_access_code_dto']
