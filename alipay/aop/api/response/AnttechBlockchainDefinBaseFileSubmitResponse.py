#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizResult import BizResult


class AnttechBlockchainDefinBaseFileSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinBaseFileSubmitResponse, self).__init__()
        self._biz_result = None

    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        if isinstance(value, BizResult):
            self._biz_result = value
        else:
            self._biz_result = BizResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinBaseFileSubmitResponse, self).parse_response_content(response_content)
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
