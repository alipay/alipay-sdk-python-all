#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LotteryPresent import LotteryPresent


class AlipayCommerceLotteryPresentlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLotteryPresentlistQueryResponse, self).__init__()
        self._results = None
        self._total_result = None

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        if isinstance(value, list):
            self._results = list()
            for i in value:
                if isinstance(i, LotteryPresent):
                    self._results.append(i)
                else:
                    self._results.append(LotteryPresent.from_alipay_dict(i))
    @property
    def total_result(self):
        return self._total_result

    @total_result.setter
    def total_result(self, value):
        self._total_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLotteryPresentlistQueryResponse, self).parse_response_content(response_content)
        if 'results' in response:
            self.results = response['results']
        if 'total_result' in response:
            self.total_result = response['total_result']
