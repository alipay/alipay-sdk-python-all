#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalOverallMetric import MedicalOverallMetric
from alipay.aop.api.domain.OrgServiceMetric import OrgServiceMetric
from alipay.aop.api.domain.ServiceTrendsMetric import ServiceTrendsMetric
from alipay.aop.api.domain.ServiceUsedMetric import ServiceUsedMetric


class AlipayCommerceMedicalInsitutionServicePreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsitutionServicePreviewResponse, self).__init__()
        self._medical_overall_metric = None
        self._org_service_metric_list = None
        self._service_trend_metric_list = None
        self._service_used_metric_list = None

    @property
    def medical_overall_metric(self):
        return self._medical_overall_metric

    @medical_overall_metric.setter
    def medical_overall_metric(self, value):
        if isinstance(value, MedicalOverallMetric):
            self._medical_overall_metric = value
        else:
            self._medical_overall_metric = MedicalOverallMetric.from_alipay_dict(value)
    @property
    def org_service_metric_list(self):
        return self._org_service_metric_list

    @org_service_metric_list.setter
    def org_service_metric_list(self, value):
        if isinstance(value, list):
            self._org_service_metric_list = list()
            for i in value:
                if isinstance(i, OrgServiceMetric):
                    self._org_service_metric_list.append(i)
                else:
                    self._org_service_metric_list.append(OrgServiceMetric.from_alipay_dict(i))
    @property
    def service_trend_metric_list(self):
        return self._service_trend_metric_list

    @service_trend_metric_list.setter
    def service_trend_metric_list(self, value):
        if isinstance(value, list):
            self._service_trend_metric_list = list()
            for i in value:
                if isinstance(i, ServiceTrendsMetric):
                    self._service_trend_metric_list.append(i)
                else:
                    self._service_trend_metric_list.append(ServiceTrendsMetric.from_alipay_dict(i))
    @property
    def service_used_metric_list(self):
        return self._service_used_metric_list

    @service_used_metric_list.setter
    def service_used_metric_list(self, value):
        if isinstance(value, list):
            self._service_used_metric_list = list()
            for i in value:
                if isinstance(i, ServiceUsedMetric):
                    self._service_used_metric_list.append(i)
                else:
                    self._service_used_metric_list.append(ServiceUsedMetric.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsitutionServicePreviewResponse, self).parse_response_content(response_content)
        if 'medical_overall_metric' in response:
            self.medical_overall_metric = response['medical_overall_metric']
        if 'org_service_metric_list' in response:
            self.org_service_metric_list = response['org_service_metric_list']
        if 'service_trend_metric_list' in response:
            self.service_trend_metric_list = response['service_trend_metric_list']
        if 'service_used_metric_list' in response:
            self.service_used_metric_list = response['service_used_metric_list']
