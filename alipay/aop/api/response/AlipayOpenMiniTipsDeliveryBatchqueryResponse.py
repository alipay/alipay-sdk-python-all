#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TipsDelivery import TipsDelivery


class AlipayOpenMiniTipsDeliveryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTipsDeliveryBatchqueryResponse, self).__init__()
        self._tips_delivery_list = None
        self._total_pages = None
        self._total_size = None

    @property
    def tips_delivery_list(self):
        return self._tips_delivery_list

    @tips_delivery_list.setter
    def tips_delivery_list(self, value):
        if isinstance(value, list):
            self._tips_delivery_list = list()
            for i in value:
                if isinstance(i, TipsDelivery):
                    self._tips_delivery_list.append(i)
                else:
                    self._tips_delivery_list.append(TipsDelivery.from_alipay_dict(i))
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTipsDeliveryBatchqueryResponse, self).parse_response_content(response_content)
        if 'tips_delivery_list' in response:
            self.tips_delivery_list = response['tips_delivery_list']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
