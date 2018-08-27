#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvMerchantInfo import IsvMerchantInfo
from alipay.aop.api.domain.ShopSummaryInfo import ShopSummaryInfo


class KoubeiMarketingToolIsvMerchantQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingToolIsvMerchantQueryResponse, self).__init__()
        self._merchant_infos = None
        self._shop_count = None
        self._shop_summary_infos = None

    @property
    def merchant_infos(self):
        return self._merchant_infos

    @merchant_infos.setter
    def merchant_infos(self, value):
        if isinstance(value, list):
            self._merchant_infos = list()
            for i in value:
                if isinstance(i, IsvMerchantInfo):
                    self._merchant_infos.append(i)
                else:
                    self._merchant_infos.append(IsvMerchantInfo.from_alipay_dict(i))
    @property
    def shop_count(self):
        return self._shop_count

    @shop_count.setter
    def shop_count(self, value):
        self._shop_count = value
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
        response = super(KoubeiMarketingToolIsvMerchantQueryResponse, self).parse_response_content(response_content)
        if 'merchant_infos' in response:
            self.merchant_infos = response['merchant_infos']
        if 'shop_count' in response:
            self.shop_count = response['shop_count']
        if 'shop_summary_infos' in response:
            self.shop_summary_infos = response['shop_summary_infos']
