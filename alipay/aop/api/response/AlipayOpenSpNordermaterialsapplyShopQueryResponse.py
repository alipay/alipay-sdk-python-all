#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopDeliveryInfo import ShopDeliveryInfo


class AlipayOpenSpNordermaterialsapplyShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyShopQueryResponse, self).__init__()
        self._materials_num = None
        self._shop_delivery_info = None

    @property
    def materials_num(self):
        return self._materials_num

    @materials_num.setter
    def materials_num(self, value):
        self._materials_num = value
    @property
    def shop_delivery_info(self):
        return self._shop_delivery_info

    @shop_delivery_info.setter
    def shop_delivery_info(self, value):
        if isinstance(value, list):
            self._shop_delivery_info = list()
            for i in value:
                if isinstance(i, ShopDeliveryInfo):
                    self._shop_delivery_info.append(i)
                else:
                    self._shop_delivery_info.append(ShopDeliveryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyShopQueryResponse, self).parse_response_content(response_content)
        if 'materials_num' in response:
            self.materials_num = response['materials_num']
        if 'shop_delivery_info' in response:
            self.shop_delivery_info = response['shop_delivery_info']
