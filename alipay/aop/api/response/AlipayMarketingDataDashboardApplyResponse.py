#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingDataDashboardApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingDataDashboardApplyResponse, self).__init__()
        self._dashboard_fail_list = None
        self._status = None

    @property
    def dashboard_fail_list(self):
        return self._dashboard_fail_list

    @dashboard_fail_list.setter
    def dashboard_fail_list(self, value):
        if isinstance(value, list):
            self._dashboard_fail_list = list()
            for i in value:
                self._dashboard_fail_list.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingDataDashboardApplyResponse, self).parse_response_content(response_content)
        if 'dashboard_fail_list' in response:
            self.dashboard_fail_list = response['dashboard_fail_list']
        if 'status' in response:
            self.status = response['status']
