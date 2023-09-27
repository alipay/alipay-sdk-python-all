#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuotaControlMetric import QuotaControlMetric


class AlipayCloudCloudbaseQuotacontrolFeeitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseQuotacontrolFeeitemQueryResponse, self).__init__()
        self._fee_items = None

    @property
    def fee_items(self):
        return self._fee_items

    @fee_items.setter
    def fee_items(self, value):
        if isinstance(value, list):
            self._fee_items = list()
            for i in value:
                if isinstance(i, QuotaControlMetric):
                    self._fee_items.append(i)
                else:
                    self._fee_items.append(QuotaControlMetric.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseQuotacontrolFeeitemQueryResponse, self).parse_response_content(response_content)
        if 'fee_items' in response:
            self.fee_items = response['fee_items']
