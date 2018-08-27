#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopCategoryConfigInfo import ShopCategoryConfigInfo


class AlipayOfflineMarketShopCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketShopCategoryQueryResponse, self).__init__()
        self._shop_category_config_infos = None

    @property
    def shop_category_config_infos(self):
        return self._shop_category_config_infos

    @shop_category_config_infos.setter
    def shop_category_config_infos(self, value):
        if isinstance(value, list):
            self._shop_category_config_infos = list()
            for i in value:
                if isinstance(i, ShopCategoryConfigInfo):
                    self._shop_category_config_infos.append(i)
                else:
                    self._shop_category_config_infos.append(ShopCategoryConfigInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketShopCategoryQueryResponse, self).parse_response_content(response_content)
        if 'shop_category_config_infos' in response:
            self.shop_category_config_infos = response['shop_category_config_infos']
