#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductSaleInfoVO import ProductSaleInfoVO


class AlipayCloudCloudpromoMallItemstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallItemstatusQueryResponse, self).__init__()
        self._product_sale_infos = None

    @property
    def product_sale_infos(self):
        return self._product_sale_infos

    @product_sale_infos.setter
    def product_sale_infos(self, value):
        if isinstance(value, list):
            self._product_sale_infos = list()
            for i in value:
                if isinstance(i, ProductSaleInfoVO):
                    self._product_sale_infos.append(i)
                else:
                    self._product_sale_infos.append(ProductSaleInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallItemstatusQueryResponse, self).parse_response_content(response_content)
        if 'product_sale_infos' in response:
            self.product_sale_infos = response['product_sale_infos']
