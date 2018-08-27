#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CityShopModel import CityShopModel


class KoubeiMerchantDepartmentShopsQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantDepartmentShopsQueryResponse, self).__init__()
        self._city_shop_models = None
        self._dept_id = None

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
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantDepartmentShopsQueryResponse, self).parse_response_content(response_content)
        if 'city_shop_models' in response:
            self.city_shop_models = response['city_shop_models']
        if 'dept_id' in response:
            self.dept_id = response['dept_id']
