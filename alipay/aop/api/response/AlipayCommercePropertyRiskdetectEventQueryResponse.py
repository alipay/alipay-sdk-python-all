#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EvnetResultVO import EvnetResultVO


class AlipayCommercePropertyRiskdetectEventQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyRiskdetectEventQueryResponse, self).__init__()
        self._event_results = None
        self._total = None

    @property
    def event_results(self):
        return self._event_results

    @event_results.setter
    def event_results(self, value):
        if isinstance(value, list):
            self._event_results = list()
            for i in value:
                if isinstance(i, EvnetResultVO):
                    self._event_results.append(i)
                else:
                    self._event_results.append(EvnetResultVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyRiskdetectEventQueryResponse, self).parse_response_content(response_content)
        if 'event_results' in response:
            self.event_results = response['event_results']
        if 'total' in response:
            self.total = response['total']
