#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TransferResultInfo import TransferResultInfo


class AlipayMarketingToolXuanyitestCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolXuanyitestCreateResponse, self).__init__()
        self._test_12 = None

    @property
    def test_12(self):
        return self._test_12

    @test_12.setter
    def test_12(self, value):
        if isinstance(value, list):
            self._test_12 = list()
            for i in value:
                if isinstance(i, TransferResultInfo):
                    self._test_12.append(i)
                else:
                    self._test_12.append(TransferResultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolXuanyitestCreateResponse, self).parse_response_content(response_content)
        if 'test_12' in response:
            self.test_12 = response['test_12']
