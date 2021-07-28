#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommonPrizeModelVo import CommonPrizeModelVo


class AlipayFundCouponWufuLiveAcceptResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuLiveAcceptResponse, self).__init__()
        self._prize_list = None
        self._prized = None

    @property
    def prize_list(self):
        return self._prize_list

    @prize_list.setter
    def prize_list(self, value):
        if isinstance(value, list):
            self._prize_list = list()
            for i in value:
                if isinstance(i, CommonPrizeModelVo):
                    self._prize_list.append(i)
                else:
                    self._prize_list.append(CommonPrizeModelVo.from_alipay_dict(i))
    @property
    def prized(self):
        return self._prized

    @prized.setter
    def prized(self, value):
        self._prized = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuLiveAcceptResponse, self).parse_response_content(response_content)
        if 'prize_list' in response:
            self.prize_list = response['prize_list']
        if 'prized' in response:
            self.prized = response['prized']
