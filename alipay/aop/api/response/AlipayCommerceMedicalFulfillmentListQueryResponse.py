#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FulfillmentInfoVO import FulfillmentInfoVO


class AlipayCommerceMedicalFulfillmentListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalFulfillmentListQueryResponse, self).__init__()
        self._fulfillment_info_list = None

    @property
    def fulfillment_info_list(self):
        return self._fulfillment_info_list

    @fulfillment_info_list.setter
    def fulfillment_info_list(self, value):
        if isinstance(value, list):
            self._fulfillment_info_list = list()
            for i in value:
                if isinstance(i, FulfillmentInfoVO):
                    self._fulfillment_info_list.append(i)
                else:
                    self._fulfillment_info_list.append(FulfillmentInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalFulfillmentListQueryResponse, self).parse_response_content(response_content)
        if 'fulfillment_info_list' in response:
            self.fulfillment_info_list = response['fulfillment_info_list']
