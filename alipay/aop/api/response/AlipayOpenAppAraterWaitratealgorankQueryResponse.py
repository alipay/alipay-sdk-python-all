#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WaitRateAlgoItem import WaitRateAlgoItem


class AlipayOpenAppAraterWaitratealgorankQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAraterWaitratealgorankQueryResponse, self).__init__()
        self._wait_rate_rank_items = None

    @property
    def wait_rate_rank_items(self):
        return self._wait_rate_rank_items

    @wait_rate_rank_items.setter
    def wait_rate_rank_items(self, value):
        if isinstance(value, list):
            self._wait_rate_rank_items = list()
            for i in value:
                if isinstance(i, WaitRateAlgoItem):
                    self._wait_rate_rank_items.append(i)
                else:
                    self._wait_rate_rank_items.append(WaitRateAlgoItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAraterWaitratealgorankQueryResponse, self).parse_response_content(response_content)
        if 'wait_rate_rank_items' in response:
            self.wait_rate_rank_items = response['wait_rate_rank_items']
