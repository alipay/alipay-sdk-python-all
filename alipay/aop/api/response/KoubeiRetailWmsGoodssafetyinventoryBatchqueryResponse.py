#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GoodsSafetyInventoryVO import GoodsSafetyInventoryVO


class KoubeiRetailWmsGoodssafetyinventoryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsGoodssafetyinventoryBatchqueryResponse, self).__init__()
        self._goods_safety_inventory_vo_list = None

    @property
    def goods_safety_inventory_vo_list(self):
        return self._goods_safety_inventory_vo_list

    @goods_safety_inventory_vo_list.setter
    def goods_safety_inventory_vo_list(self, value):
        if isinstance(value, list):
            self._goods_safety_inventory_vo_list = list()
            for i in value:
                if isinstance(i, GoodsSafetyInventoryVO):
                    self._goods_safety_inventory_vo_list.append(i)
                else:
                    self._goods_safety_inventory_vo_list.append(GoodsSafetyInventoryVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsGoodssafetyinventoryBatchqueryResponse, self).parse_response_content(response_content)
        if 'goods_safety_inventory_vo_list' in response:
            self.goods_safety_inventory_vo_list = response['goods_safety_inventory_vo_list']
