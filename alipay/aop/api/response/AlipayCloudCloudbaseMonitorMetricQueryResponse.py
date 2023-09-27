#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseMonitorMetricQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorMetricQueryResponse, self).__init__()
        self._metrics = None

    @property
    def metrics(self):
        return self._metrics

    @metrics.setter
    def metrics(self, value):
        self._metrics = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorMetricQueryResponse, self).parse_response_content(response_content)
        if 'metrics' in response:
            self.metrics = response['metrics']
