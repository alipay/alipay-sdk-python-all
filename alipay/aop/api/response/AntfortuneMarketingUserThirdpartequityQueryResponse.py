#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FinEquityInfo import FinEquityInfo


class AntfortuneMarketingUserThirdpartequityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneMarketingUserThirdpartequityQueryResponse, self).__init__()
        self._equity_info = None
        self._should_retry = None

    @property
    def equity_info(self):
        return self._equity_info

    @equity_info.setter
    def equity_info(self, value):
        if isinstance(value, list):
            self._equity_info = list()
            for i in value:
                if isinstance(i, FinEquityInfo):
                    self._equity_info.append(i)
                else:
                    self._equity_info.append(FinEquityInfo.from_alipay_dict(i))
    @property
    def should_retry(self):
        return self._should_retry

    @should_retry.setter
    def should_retry(self, value):
        self._should_retry = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneMarketingUserThirdpartequityQueryResponse, self).parse_response_content(response_content)
        if 'equity_info' in response:
            self.equity_info = response['equity_info']
        if 'should_retry' in response:
            self.should_retry = response['should_retry']
