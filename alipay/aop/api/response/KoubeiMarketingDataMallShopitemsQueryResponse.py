#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TBMiniShopBo import TBMiniShopBo


class KoubeiMarketingDataMallShopitemsQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataMallShopitemsQueryResponse, self).__init__()
        self._shop_list = None

    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, TBMiniShopBo):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(TBMiniShopBo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataMallShopitemsQueryResponse, self).parse_response_content(response_content)
        if 'shop_list' in response:
            self.shop_list = response['shop_list']
