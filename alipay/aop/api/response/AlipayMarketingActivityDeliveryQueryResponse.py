#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoDeliveryInfo import PromoDeliveryInfo


class AlipayMarketingActivityDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityDeliveryQueryResponse, self).__init__()
        self._delivery_info_list = None

    @property
    def delivery_info_list(self):
        return self._delivery_info_list

    @delivery_info_list.setter
    def delivery_info_list(self, value):
        if isinstance(value, list):
            self._delivery_info_list = list()
            for i in value:
                if isinstance(i, PromoDeliveryInfo):
                    self._delivery_info_list.append(i)
                else:
                    self._delivery_info_list.append(PromoDeliveryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'delivery_info_list' in response:
            self.delivery_info_list = response['delivery_info_list']
