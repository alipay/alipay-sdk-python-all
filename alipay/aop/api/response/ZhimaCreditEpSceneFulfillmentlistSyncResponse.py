#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FulfillmentResult import FulfillmentResult


class ZhimaCreditEpSceneFulfillmentlistSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSceneFulfillmentlistSyncResponse, self).__init__()
        self._fulfillment_result_list = None

    @property
    def fulfillment_result_list(self):
        return self._fulfillment_result_list

    @fulfillment_result_list.setter
    def fulfillment_result_list(self, value):
        if isinstance(value, list):
            self._fulfillment_result_list = list()
            for i in value:
                if isinstance(i, FulfillmentResult):
                    self._fulfillment_result_list.append(i)
                else:
                    self._fulfillment_result_list.append(FulfillmentResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSceneFulfillmentlistSyncResponse, self).parse_response_content(response_content)
        if 'fulfillment_result_list' in response:
            self.fulfillment_result_list = response['fulfillment_result_list']
