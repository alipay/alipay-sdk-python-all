#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LiveInfo import LiveInfo


class AlipayFincoreComplianceRcsmartLivecontentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceRcsmartLivecontentQueryResponse, self).__init__()
        self._live_info_list = None
        self._total_count = None

    @property
    def live_info_list(self):
        return self._live_info_list

    @live_info_list.setter
    def live_info_list(self, value):
        if isinstance(value, list):
            self._live_info_list = list()
            for i in value:
                if isinstance(i, LiveInfo):
                    self._live_info_list.append(i)
                else:
                    self._live_info_list.append(LiveInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceRcsmartLivecontentQueryResponse, self).parse_response_content(response_content)
        if 'live_info_list' in response:
            self.live_info_list = response['live_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
