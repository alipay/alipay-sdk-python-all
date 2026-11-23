#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductRelationDTO import ProductRelationDTO


class AlipayCommerceRetailCashbackrelationBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailCashbackrelationBatchqueryResponse, self).__init__()
        self._product_relation_list = None
        self._total_num = None

    @property
    def product_relation_list(self):
        return self._product_relation_list

    @product_relation_list.setter
    def product_relation_list(self, value):
        if isinstance(value, list):
            self._product_relation_list = list()
            for i in value:
                if isinstance(i, ProductRelationDTO):
                    self._product_relation_list.append(i)
                else:
                    self._product_relation_list.append(ProductRelationDTO.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailCashbackrelationBatchqueryResponse, self).parse_response_content(response_content)
        if 'product_relation_list' in response:
            self.product_relation_list = response['product_relation_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
