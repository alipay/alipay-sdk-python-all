#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PucExternalOrderDetailInfo import PucExternalOrderDetailInfo


class AlipayEbppJfExternalbillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfExternalbillCreateResponse, self).__init__()
        self._trade_detail = None

    @property
    def trade_detail(self):
        return self._trade_detail

    @trade_detail.setter
    def trade_detail(self, value):
        if isinstance(value, PucExternalOrderDetailInfo):
            self._trade_detail = value
        else:
            self._trade_detail = PucExternalOrderDetailInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfExternalbillCreateResponse, self).parse_response_content(response_content)
        if 'trade_detail' in response:
            self.trade_detail = response['trade_detail']
