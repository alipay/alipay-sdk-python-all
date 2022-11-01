#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketingDeliveryDetail import MarketingDeliveryDetail


class AlipayOpenMiniTemplatemsgMaketingBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTemplatemsgMaketingBatchqueryResponse, self).__init__()
        self._marketing_delivery_detail_list = None
        self._total = None

    @property
    def marketing_delivery_detail_list(self):
        return self._marketing_delivery_detail_list

    @marketing_delivery_detail_list.setter
    def marketing_delivery_detail_list(self, value):
        if isinstance(value, list):
            self._marketing_delivery_detail_list = list()
            for i in value:
                if isinstance(i, MarketingDeliveryDetail):
                    self._marketing_delivery_detail_list.append(i)
                else:
                    self._marketing_delivery_detail_list.append(MarketingDeliveryDetail.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTemplatemsgMaketingBatchqueryResponse, self).parse_response_content(response_content)
        if 'marketing_delivery_detail_list' in response:
            self.marketing_delivery_detail_list = response['marketing_delivery_detail_list']
        if 'total' in response:
            self.total = response['total']
