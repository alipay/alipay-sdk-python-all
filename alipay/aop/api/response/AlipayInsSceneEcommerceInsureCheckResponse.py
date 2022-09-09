#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsureAdmitDetailResultDTO import InsureAdmitDetailResultDTO


class AlipayInsSceneEcommerceInsureCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceInsureCheckResponse, self).__init__()
        self._admit_result = None

    @property
    def admit_result(self):
        return self._admit_result

    @admit_result.setter
    def admit_result(self, value):
        if isinstance(value, list):
            self._admit_result = list()
            for i in value:
                if isinstance(i, InsureAdmitDetailResultDTO):
                    self._admit_result.append(i)
                else:
                    self._admit_result.append(InsureAdmitDetailResultDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceInsureCheckResponse, self).parse_response_content(response_content)
        if 'admit_result' in response:
            self.admit_result = response['admit_result']
