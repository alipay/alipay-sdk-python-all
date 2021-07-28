#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorCodeDTO import ErrorCodeDTO
from alipay.aop.api.domain.JsApiBaseDTO import JsApiBaseDTO


class AlipayOpenMiniAliminiabilityprodJsapiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAliminiabilityprodJsapiQueryResponse, self).__init__()
        self._error_code_dto_list = None
        self._in_params = None
        self._js_api_base_dto = None
        self._out_params = None

    @property
    def error_code_dto_list(self):
        return self._error_code_dto_list

    @error_code_dto_list.setter
    def error_code_dto_list(self, value):
        if isinstance(value, list):
            self._error_code_dto_list = list()
            for i in value:
                if isinstance(i, ErrorCodeDTO):
                    self._error_code_dto_list.append(i)
                else:
                    self._error_code_dto_list.append(ErrorCodeDTO.from_alipay_dict(i))
    @property
    def in_params(self):
        return self._in_params

    @in_params.setter
    def in_params(self, value):
        self._in_params = value
    @property
    def js_api_base_dto(self):
        return self._js_api_base_dto

    @js_api_base_dto.setter
    def js_api_base_dto(self, value):
        if isinstance(value, JsApiBaseDTO):
            self._js_api_base_dto = value
        else:
            self._js_api_base_dto = JsApiBaseDTO.from_alipay_dict(value)
    @property
    def out_params(self):
        return self._out_params

    @out_params.setter
    def out_params(self, value):
        self._out_params = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAliminiabilityprodJsapiQueryResponse, self).parse_response_content(response_content)
        if 'error_code_dto_list' in response:
            self.error_code_dto_list = response['error_code_dto_list']
        if 'in_params' in response:
            self.in_params = response['in_params']
        if 'js_api_base_dto' in response:
            self.js_api_base_dto = response['js_api_base_dto']
        if 'out_params' in response:
            self.out_params = response['out_params']
