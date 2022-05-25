#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessParams import AccessParams
from alipay.aop.api.domain.MerchantCard import MerchantCard


class AntOcrTesConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntOcrTesConsultResponse, self).__init__()
        self._hhgghfghj = None
        self._ppds = None
        self._test_3 = None

    @property
    def hhgghfghj(self):
        return self._hhgghfghj

    @hhgghfghj.setter
    def hhgghfghj(self, value):
        if isinstance(value, AccessParams):
            self._hhgghfghj = value
        else:
            self._hhgghfghj = AccessParams.from_alipay_dict(value)
    @property
    def ppds(self):
        return self._ppds

    @ppds.setter
    def ppds(self, value):
        self._ppds = value
    @property
    def test_3(self):
        return self._test_3

    @test_3.setter
    def test_3(self, value):
        if isinstance(value, MerchantCard):
            self._test_3 = value
        else:
            self._test_3 = MerchantCard.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntOcrTesConsultResponse, self).parse_response_content(response_content)
        if 'hhgghfghj' in response:
            self.hhgghfghj = response['hhgghfghj']
        if 'ppds' in response:
            self.ppds = response['ppds']
        if 'test_3' in response:
            self.test_3 = response['test_3']
