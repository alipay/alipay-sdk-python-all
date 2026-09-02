#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EvaluationOrderInfo import EvaluationOrderInfo


class ZhimaCreditEpEvaluationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpEvaluationQueryResponse, self).__init__()
        self._order_list = None

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, EvaluationOrderInfo):
                    self._order_list.append(i)
                else:
                    self._order_list.append(EvaluationOrderInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpEvaluationQueryResponse, self).parse_response_content(response_content)
        if 'order_list' in response:
            self.order_list = response['order_list']
