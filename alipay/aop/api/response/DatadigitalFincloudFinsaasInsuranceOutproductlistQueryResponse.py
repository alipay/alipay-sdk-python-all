#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OuterProductVO import OuterProductVO


class DatadigitalFincloudFinsaasInsuranceOutproductlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasInsuranceOutproductlistQueryResponse, self).__init__()
        self._outer_product_items = None

    @property
    def outer_product_items(self):
        return self._outer_product_items

    @outer_product_items.setter
    def outer_product_items(self, value):
        if isinstance(value, list):
            self._outer_product_items = list()
            for i in value:
                if isinstance(i, OuterProductVO):
                    self._outer_product_items.append(i)
                else:
                    self._outer_product_items.append(OuterProductVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasInsuranceOutproductlistQueryResponse, self).parse_response_content(response_content)
        if 'outer_product_items' in response:
            self.outer_product_items = response['outer_product_items']
