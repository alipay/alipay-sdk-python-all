#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassInfoOpenApiModel import PassInfoOpenApiModel


class AlipayUserPassGrouplistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPassGrouplistQueryResponse, self).__init__()
        self._pass_info_list = None

    @property
    def pass_info_list(self):
        return self._pass_info_list

    @pass_info_list.setter
    def pass_info_list(self, value):
        if isinstance(value, list):
            self._pass_info_list = list()
            for i in value:
                if isinstance(i, PassInfoOpenApiModel):
                    self._pass_info_list.append(i)
                else:
                    self._pass_info_list.append(PassInfoOpenApiModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserPassGrouplistQueryResponse, self).parse_response_content(response_content)
        if 'pass_info_list' in response:
            self.pass_info_list = response['pass_info_list']
