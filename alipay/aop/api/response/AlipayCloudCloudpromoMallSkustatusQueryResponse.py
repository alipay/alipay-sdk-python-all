#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SkuSaleInfoVO import SkuSaleInfoVO


class AlipayCloudCloudpromoMallSkustatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallSkustatusQueryResponse, self).__init__()
        self._sku_sale_infos = None

    @property
    def sku_sale_infos(self):
        return self._sku_sale_infos

    @sku_sale_infos.setter
    def sku_sale_infos(self, value):
        if isinstance(value, list):
            self._sku_sale_infos = list()
            for i in value:
                if isinstance(i, SkuSaleInfoVO):
                    self._sku_sale_infos.append(i)
                else:
                    self._sku_sale_infos.append(SkuSaleInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallSkustatusQueryResponse, self).parse_response_content(response_content)
        if 'sku_sale_infos' in response:
            self.sku_sale_infos = response['sku_sale_infos']
