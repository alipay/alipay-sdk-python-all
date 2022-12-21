#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommonPrizeVo import CommonPrizeVo


class AlipayFundCouponWufuCardApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuCardApplyResponse, self).__init__()
        self._prize_list = None

    @property
    def prize_list(self):
        return self._prize_list

    @prize_list.setter
    def prize_list(self, value):
        if isinstance(value, list):
            self._prize_list = list()
            for i in value:
                if isinstance(i, CommonPrizeVo):
                    self._prize_list.append(i)
                else:
                    self._prize_list.append(CommonPrizeVo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuCardApplyResponse, self).parse_response_content(response_content)
        if 'prize_list' in response:
            self.prize_list = response['prize_list']
