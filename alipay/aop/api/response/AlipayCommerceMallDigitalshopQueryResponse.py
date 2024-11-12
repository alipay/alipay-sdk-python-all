#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DigitalShopInfo import DigitalShopInfo


class AlipayCommerceMallDigitalshopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMallDigitalshopQueryResponse, self).__init__()
        self._digital_shop_list = None
        self._mall_id = None
        self._mall_name = None

    @property
    def digital_shop_list(self):
        return self._digital_shop_list

    @digital_shop_list.setter
    def digital_shop_list(self, value):
        if isinstance(value, list):
            self._digital_shop_list = list()
            for i in value:
                if isinstance(i, DigitalShopInfo):
                    self._digital_shop_list.append(i)
                else:
                    self._digital_shop_list.append(DigitalShopInfo.from_alipay_dict(i))
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def mall_name(self):
        return self._mall_name

    @mall_name.setter
    def mall_name(self, value):
        self._mall_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMallDigitalshopQueryResponse, self).parse_response_content(response_content)
        if 'digital_shop_list' in response:
            self.digital_shop_list = response['digital_shop_list']
        if 'mall_id' in response:
            self.mall_id = response['mall_id']
        if 'mall_name' in response:
            self.mall_name = response['mall_name']
