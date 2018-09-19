#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessOrdersFeedBackResult import AccessOrdersFeedBackResult


class KoubeiSalesKbassetStuffOrdersresultSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffOrdersresultSyncResponse, self).__init__()
        self._orders_feedback_result = None

    @property
    def orders_feedback_result(self):
        return self._orders_feedback_result

    @orders_feedback_result.setter
    def orders_feedback_result(self, value):
        if isinstance(value, list):
            self._orders_feedback_result = list()
            for i in value:
                if isinstance(i, AccessOrdersFeedBackResult):
                    self._orders_feedback_result.append(i)
                else:
                    self._orders_feedback_result.append(AccessOrdersFeedBackResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffOrdersresultSyncResponse, self).parse_response_content(response_content)
        if 'orders_feedback_result' in response:
            self.orders_feedback_result = response['orders_feedback_result']
