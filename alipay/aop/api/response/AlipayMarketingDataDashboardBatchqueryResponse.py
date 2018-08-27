#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DashBoardMeta import DashBoardMeta


class AlipayMarketingDataDashboardBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingDataDashboardBatchqueryResponse, self).__init__()
        self._dashboard_list = None
        self._total_page_count = None

    @property
    def dashboard_list(self):
        return self._dashboard_list

    @dashboard_list.setter
    def dashboard_list(self, value):
        if isinstance(value, list):
            self._dashboard_list = list()
            for i in value:
                if isinstance(i, DashBoardMeta):
                    self._dashboard_list.append(i)
                else:
                    self._dashboard_list.append(DashBoardMeta.from_alipay_dict(i))
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingDataDashboardBatchqueryResponse, self).parse_response_content(response_content)
        if 'dashboard_list' in response:
            self.dashboard_list = response['dashboard_list']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
