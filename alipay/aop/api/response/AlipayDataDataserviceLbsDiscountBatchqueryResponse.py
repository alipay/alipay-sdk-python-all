#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntlbsKBDiscountInfo import AntlbsKBDiscountInfo


class AlipayDataDataserviceLbsDiscountBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceLbsDiscountBatchqueryResponse, self).__init__()
        self._discounts = None

    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, value):
        if isinstance(value, list):
            self._discounts = list()
            for i in value:
                if isinstance(i, AntlbsKBDiscountInfo):
                    self._discounts.append(i)
                else:
                    self._discounts.append(AntlbsKBDiscountInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceLbsDiscountBatchqueryResponse, self).parse_response_content(response_content)
        if 'discounts' in response:
            self.discounts = response['discounts']
