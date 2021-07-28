#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopQueryOpenApiVO import ShopQueryOpenApiVO


class AntMerchantExpandShopPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandShopPageQueryResponse, self).__init__()
        self._shop_infos = None
        self._total_pages = None

    @property
    def shop_infos(self):
        return self._shop_infos

    @shop_infos.setter
    def shop_infos(self, value):
        if isinstance(value, list):
            self._shop_infos = list()
            for i in value:
                if isinstance(i, ShopQueryOpenApiVO):
                    self._shop_infos.append(i)
                else:
                    self._shop_infos.append(ShopQueryOpenApiVO.from_alipay_dict(i))
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandShopPageQueryResponse, self).parse_response_content(response_content)
        if 'shop_infos' in response:
            self.shop_infos = response['shop_infos']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
