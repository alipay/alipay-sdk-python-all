#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopPromoInfo import ShopPromoInfo


class KoubeiMarketingMallShoppromoinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingMallShoppromoinfoQueryResponse, self).__init__()
        self._shop_promo_infos = None

    @property
    def shop_promo_infos(self):
        return self._shop_promo_infos

    @shop_promo_infos.setter
    def shop_promo_infos(self, value):
        if isinstance(value, list):
            self._shop_promo_infos = list()
            for i in value:
                if isinstance(i, ShopPromoInfo):
                    self._shop_promo_infos.append(i)
                else:
                    self._shop_promo_infos.append(ShopPromoInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingMallShoppromoinfoQueryResponse, self).parse_response_content(response_content)
        if 'shop_promo_infos' in response:
            self.shop_promo_infos = response['shop_promo_infos']
