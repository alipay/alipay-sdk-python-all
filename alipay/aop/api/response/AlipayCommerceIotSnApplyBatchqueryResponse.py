#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SnApplyInfo import SnApplyInfo


class AlipayCommerceIotSnApplyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotSnApplyBatchqueryResponse, self).__init__()
        self._apply_list = None
        self._total = None

    @property
    def apply_list(self):
        return self._apply_list

    @apply_list.setter
    def apply_list(self, value):
        if isinstance(value, list):
            self._apply_list = list()
            for i in value:
                if isinstance(i, SnApplyInfo):
                    self._apply_list.append(i)
                else:
                    self._apply_list.append(SnApplyInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotSnApplyBatchqueryResponse, self).parse_response_content(response_content)
        if 'apply_list' in response:
            self.apply_list = response['apply_list']
        if 'total' in response:
            self.total = response['total']
