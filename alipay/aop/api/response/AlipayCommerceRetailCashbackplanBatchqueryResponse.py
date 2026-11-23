#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CashbackDeliveryPlanVO import CashbackDeliveryPlanVO


class AlipayCommerceRetailCashbackplanBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailCashbackplanBatchqueryResponse, self).__init__()
        self._delivery_plan_list = None
        self._total_num = None

    @property
    def delivery_plan_list(self):
        return self._delivery_plan_list

    @delivery_plan_list.setter
    def delivery_plan_list(self, value):
        if isinstance(value, list):
            self._delivery_plan_list = list()
            for i in value:
                if isinstance(i, CashbackDeliveryPlanVO):
                    self._delivery_plan_list.append(i)
                else:
                    self._delivery_plan_list.append(CashbackDeliveryPlanVO.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailCashbackplanBatchqueryResponse, self).parse_response_content(response_content)
        if 'delivery_plan_list' in response:
            self.delivery_plan_list = response['delivery_plan_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
