#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BailDetailResult import BailDetailResult


class AlipayDataBillBailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataBillBailQueryResponse, self).__init__()
        self._detail_list = None

    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, BailDetailResult):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(BailDetailResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataBillBailQueryResponse, self).parse_response_content(response_content)
        if 'detail_list' in response:
            self.detail_list = response['detail_list']
