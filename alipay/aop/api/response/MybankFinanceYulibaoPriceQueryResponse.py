#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YLBPriceDetailInfo import YLBPriceDetailInfo


class MybankFinanceYulibaoPriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankFinanceYulibaoPriceQueryResponse, self).__init__()
        self._ylb_price_detail_infos = None

    @property
    def ylb_price_detail_infos(self):
        return self._ylb_price_detail_infos

    @ylb_price_detail_infos.setter
    def ylb_price_detail_infos(self, value):
        if isinstance(value, list):
            self._ylb_price_detail_infos = list()
            for i in value:
                if isinstance(i, YLBPriceDetailInfo):
                    self._ylb_price_detail_infos.append(i)
                else:
                    self._ylb_price_detail_infos.append(YLBPriceDetailInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankFinanceYulibaoPriceQueryResponse, self).parse_response_content(response_content)
        if 'ylb_price_detail_infos' in response:
            self.ylb_price_detail_infos = response['ylb_price_detail_infos']
