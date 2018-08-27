#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CityShopModel import CityShopModel


class KoubeiMerchantShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantShopQueryResponse, self).__init__()
        self._city_shop_models = None

    @property
    def city_shop_models(self):
        return self._city_shop_models

    @city_shop_models.setter
    def city_shop_models(self, value):
        if isinstance(value, list):
            self._city_shop_models = list()
            for i in value:
                if isinstance(i, CityShopModel):
                    self._city_shop_models.append(i)
                else:
                    self._city_shop_models.append(CityShopModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantShopQueryResponse, self).parse_response_content(response_content)
        if 'city_shop_models' in response:
            self.city_shop_models = response['city_shop_models']
