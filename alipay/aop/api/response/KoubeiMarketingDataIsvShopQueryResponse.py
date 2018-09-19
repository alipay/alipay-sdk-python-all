#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopSummaryInfo import ShopSummaryInfo


class KoubeiMarketingDataIsvShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataIsvShopQueryResponse, self).__init__()
        self._shop_summary_infos = None

    @property
    def shop_summary_infos(self):
        return self._shop_summary_infos

    @shop_summary_infos.setter
    def shop_summary_infos(self, value):
        if isinstance(value, list):
            self._shop_summary_infos = list()
            for i in value:
                if isinstance(i, ShopSummaryInfo):
                    self._shop_summary_infos.append(i)
                else:
                    self._shop_summary_infos.append(ShopSummaryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataIsvShopQueryResponse, self).parse_response_content(response_content)
        if 'shop_summary_infos' in response:
            self.shop_summary_infos = response['shop_summary_infos']
