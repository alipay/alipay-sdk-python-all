#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BroadcastReportItem import BroadcastReportItem


class AlipayOfflineProviderBroadcastQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderBroadcastQueryResponse, self).__init__()
        self._broadcast_report_list = None

    @property
    def broadcast_report_list(self):
        return self._broadcast_report_list

    @broadcast_report_list.setter
    def broadcast_report_list(self, value):
        if isinstance(value, list):
            self._broadcast_report_list = list()
            for i in value:
                if isinstance(i, BroadcastReportItem):
                    self._broadcast_report_list.append(i)
                else:
                    self._broadcast_report_list.append(BroadcastReportItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderBroadcastQueryResponse, self).parse_response_content(response_content)
        if 'broadcast_report_list' in response:
            self.broadcast_report_list = response['broadcast_report_list']
