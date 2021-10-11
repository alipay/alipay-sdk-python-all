#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessRelationShopDetailInfo import BusinessRelationShopDetailInfo


class AlipayBusinessRelationShopdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationShopdetailQueryResponse, self).__init__()
        self._shop_info = None

    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, BusinessRelationShopDetailInfo):
            self._shop_info = value
        else:
            self._shop_info = BusinessRelationShopDetailInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationShopdetailQueryResponse, self).parse_response_content(response_content)
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
