#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandStoreShopserviceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandStoreShopserviceCreateResponse, self).__init__()
        self._out_biz_no = None
        self._shop_service_id = None
        self._sku_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def shop_service_id(self):
        return self._shop_service_id

    @shop_service_id.setter
    def shop_service_id(self, value):
        self._shop_service_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandStoreShopserviceCreateResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'shop_service_id' in response:
            self.shop_service_id = response['shop_service_id']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
