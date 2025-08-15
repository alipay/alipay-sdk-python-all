#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EquityServiceInfo import EquityServiceInfo


class AlipayCommerceMedicalInsurancePerformstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsurancePerformstatusQueryResponse, self).__init__()
        self._service_list = None
        self._status = None

    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, EquityServiceInfo):
                    self._service_list.append(i)
                else:
                    self._service_list.append(EquityServiceInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsurancePerformstatusQueryResponse, self).parse_response_content(response_content)
        if 'service_list' in response:
            self.service_list = response['service_list']
        if 'status' in response:
            self.status = response['status']
