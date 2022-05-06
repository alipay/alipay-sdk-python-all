#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessRelationChangeShopInfo import BusinessRelationChangeShopInfo


class AlipayBusinessRelationChangeshopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationChangeshopBatchqueryResponse, self).__init__()
        self._change_shop_infos = None

    @property
    def change_shop_infos(self):
        return self._change_shop_infos

    @change_shop_infos.setter
    def change_shop_infos(self, value):
        if isinstance(value, list):
            self._change_shop_infos = list()
            for i in value:
                if isinstance(i, BusinessRelationChangeShopInfo):
                    self._change_shop_infos.append(i)
                else:
                    self._change_shop_infos.append(BusinessRelationChangeShopInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationChangeshopBatchqueryResponse, self).parse_response_content(response_content)
        if 'change_shop_infos' in response:
            self.change_shop_infos = response['change_shop_infos']
