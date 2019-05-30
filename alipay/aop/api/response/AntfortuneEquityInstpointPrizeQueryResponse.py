#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointPrizeInfo import PointPrizeInfo


class AntfortuneEquityInstpointPrizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityInstpointPrizeQueryResponse, self).__init__()
        self._prize_info = None
        self._total_count = None

    @property
    def prize_info(self):
        return self._prize_info

    @prize_info.setter
    def prize_info(self, value):
        if isinstance(value, list):
            self._prize_info = list()
            for i in value:
                if isinstance(i, PointPrizeInfo):
                    self._prize_info.append(i)
                else:
                    self._prize_info.append(PointPrizeInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityInstpointPrizeQueryResponse, self).parse_response_content(response_content)
        if 'prize_info' in response:
            self.prize_info = response['prize_info']
        if 'total_count' in response:
            self.total_count = response['total_count']
