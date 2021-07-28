#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessRelationShopInfo import BusinessRelationShopInfo


class AlipayBusinessRelationShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationShopQueryResponse, self).__init__()
        self._shop_infos = None

    @property
    def shop_infos(self):
        return self._shop_infos

    @shop_infos.setter
    def shop_infos(self, value):
        if isinstance(value, list):
            self._shop_infos = list()
            for i in value:
                if isinstance(i, BusinessRelationShopInfo):
                    self._shop_infos.append(i)
                else:
                    self._shop_infos.append(BusinessRelationShopInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationShopQueryResponse, self).parse_response_content(response_content)
        if 'shop_infos' in response:
            self.shop_infos = response['shop_infos']
