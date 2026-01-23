#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityDiscountInfo import ActivityDiscountInfo


class AlipayCommerceActivityDiscountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceActivityDiscountQueryResponse, self).__init__()
        self._discount_activity_info_list = None

    @property
    def discount_activity_info_list(self):
        return self._discount_activity_info_list

    @discount_activity_info_list.setter
    def discount_activity_info_list(self, value):
        if isinstance(value, list):
            self._discount_activity_info_list = list()
            for i in value:
                if isinstance(i, ActivityDiscountInfo):
                    self._discount_activity_info_list.append(i)
                else:
                    self._discount_activity_info_list.append(ActivityDiscountInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceActivityDiscountQueryResponse, self).parse_response_content(response_content)
        if 'discount_activity_info_list' in response:
            self.discount_activity_info_list = response['discount_activity_info_list']
