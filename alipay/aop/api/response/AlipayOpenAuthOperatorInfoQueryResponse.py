#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperatorBasicInfo import OperatorBasicInfo


class AlipayOpenAuthOperatorInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthOperatorInfoQueryResponse, self).__init__()
        self._operator_info = None

    @property
    def operator_info(self):
        return self._operator_info

    @operator_info.setter
    def operator_info(self, value):
        if isinstance(value, OperatorBasicInfo):
            self._operator_info = value
        else:
            self._operator_info = OperatorBasicInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthOperatorInfoQueryResponse, self).parse_response_content(response_content)
        if 'operator_info' in response:
            self.operator_info = response['operator_info']
