#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdReportMetricDetail import AdReportMetricDetail


class AlipayDataDataserviceAdReportmetricQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdReportmetricQueryResponse, self).__init__()
        self._metric_list = None
        self._total = None

    @property
    def metric_list(self):
        return self._metric_list

    @metric_list.setter
    def metric_list(self, value):
        if isinstance(value, list):
            self._metric_list = list()
            for i in value:
                if isinstance(i, AdReportMetricDetail):
                    self._metric_list.append(i)
                else:
                    self._metric_list.append(AdReportMetricDetail.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdReportmetricQueryResponse, self).parse_response_content(response_content)
        if 'metric_list' in response:
            self.metric_list = response['metric_list']
        if 'total' in response:
            self.total = response['total']
