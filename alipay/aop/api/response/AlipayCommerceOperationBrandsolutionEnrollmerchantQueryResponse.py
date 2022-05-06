#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantActivityGoods import MerchantActivityGoods


class AlipayCommerceOperationBrandsolutionEnrollmerchantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBrandsolutionEnrollmerchantQueryResponse, self).__init__()
        self._activity_status = None
        self._merchant_activity_goods_benefit = None

    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def merchant_activity_goods_benefit(self):
        return self._merchant_activity_goods_benefit

    @merchant_activity_goods_benefit.setter
    def merchant_activity_goods_benefit(self, value):
        if isinstance(value, list):
            self._merchant_activity_goods_benefit = list()
            for i in value:
                if isinstance(i, MerchantActivityGoods):
                    self._merchant_activity_goods_benefit.append(i)
                else:
                    self._merchant_activity_goods_benefit.append(MerchantActivityGoods.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBrandsolutionEnrollmerchantQueryResponse, self).parse_response_content(response_content)
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'merchant_activity_goods_benefit' in response:
            self.merchant_activity_goods_benefit = response['merchant_activity_goods_benefit']
