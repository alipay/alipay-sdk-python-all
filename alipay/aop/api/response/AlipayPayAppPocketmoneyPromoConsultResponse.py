#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WatchPromoPrizeDetail import WatchPromoPrizeDetail


class AlipayPayAppPocketmoneyPromoConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppPocketmoneyPromoConsultResponse, self).__init__()
        self._prize_detail = None

    @property
    def prize_detail(self):
        return self._prize_detail

    @prize_detail.setter
    def prize_detail(self, value):
        if isinstance(value, WatchPromoPrizeDetail):
            self._prize_detail = value
        else:
            self._prize_detail = WatchPromoPrizeDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppPocketmoneyPromoConsultResponse, self).parse_response_content(response_content)
        if 'prize_detail' in response:
            self.prize_detail = response['prize_detail']
