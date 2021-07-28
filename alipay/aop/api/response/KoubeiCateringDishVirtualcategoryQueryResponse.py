#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishVirtualShopSimplifyInfo import KbdishVirtualShopSimplifyInfo


class KoubeiCateringDishVirtualcategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishVirtualcategoryQueryResponse, self).__init__()
        self._retry = None
        self._shop_info = None

    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, KbdishVirtualShopSimplifyInfo):
            self._shop_info = value
        else:
            self._shop_info = KbdishVirtualShopSimplifyInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishVirtualcategoryQueryResponse, self).parse_response_content(response_content)
        if 'retry' in response:
            self.retry = response['retry']
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
