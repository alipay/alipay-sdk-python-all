#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopProductPriceList import ShopProductPriceList


class AlipayCommerceEcShopProductpriceModifyModel(object):

    def __init__(self):
        self._merchant_enterprise_id = None
        self._service_provider_id = None
        self._shop_product_price_list = None

    @property
    def merchant_enterprise_id(self):
        return self._merchant_enterprise_id

    @merchant_enterprise_id.setter
    def merchant_enterprise_id(self, value):
        self._merchant_enterprise_id = value
    @property
    def service_provider_id(self):
        return self._service_provider_id

    @service_provider_id.setter
    def service_provider_id(self, value):
        self._service_provider_id = value
    @property
    def shop_product_price_list(self):
        return self._shop_product_price_list

    @shop_product_price_list.setter
    def shop_product_price_list(self, value):
        if isinstance(value, list):
            self._shop_product_price_list = list()
            for i in value:
                if isinstance(i, ShopProductPriceList):
                    self._shop_product_price_list.append(i)
                else:
                    self._shop_product_price_list.append(ShopProductPriceList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_enterprise_id:
            if hasattr(self.merchant_enterprise_id, 'to_alipay_dict'):
                params['merchant_enterprise_id'] = self.merchant_enterprise_id.to_alipay_dict()
            else:
                params['merchant_enterprise_id'] = self.merchant_enterprise_id
        if self.service_provider_id:
            if hasattr(self.service_provider_id, 'to_alipay_dict'):
                params['service_provider_id'] = self.service_provider_id.to_alipay_dict()
            else:
                params['service_provider_id'] = self.service_provider_id
        if self.shop_product_price_list:
            if isinstance(self.shop_product_price_list, list):
                for i in range(0, len(self.shop_product_price_list)):
                    element = self.shop_product_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_product_price_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_product_price_list, 'to_alipay_dict'):
                params['shop_product_price_list'] = self.shop_product_price_list.to_alipay_dict()
            else:
                params['shop_product_price_list'] = self.shop_product_price_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcShopProductpriceModifyModel()
        if 'merchant_enterprise_id' in d:
            o.merchant_enterprise_id = d['merchant_enterprise_id']
        if 'service_provider_id' in d:
            o.service_provider_id = d['service_provider_id']
        if 'shop_product_price_list' in d:
            o.shop_product_price_list = d['shop_product_price_list']
        return o


