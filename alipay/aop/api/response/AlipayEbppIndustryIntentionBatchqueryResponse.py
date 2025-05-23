#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntentionBaseInfo import IntentionBaseInfo


class AlipayEbppIndustryIntentionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryIntentionBatchqueryResponse, self).__init__()
        self._intention_list = None

    @property
    def intention_list(self):
        return self._intention_list

    @intention_list.setter
    def intention_list(self, value):
        if isinstance(value, list):
            self._intention_list = list()
            for i in value:
                if isinstance(i, IntentionBaseInfo):
                    self._intention_list.append(i)
                else:
                    self._intention_list.append(IntentionBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryIntentionBatchqueryResponse, self).parse_response_content(response_content)
        if 'intention_list' in response:
            self.intention_list = response['intention_list']
