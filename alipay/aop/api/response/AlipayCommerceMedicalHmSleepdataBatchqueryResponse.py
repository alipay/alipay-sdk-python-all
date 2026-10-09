#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalHmDailySleepRecord import MedicalHmDailySleepRecord


class AlipayCommerceMedicalHmSleepdataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmSleepdataBatchqueryResponse, self).__init__()
        self._is_hardware_device_bound = None
        self._sleepdata_list = None

    @property
    def is_hardware_device_bound(self):
        return self._is_hardware_device_bound

    @is_hardware_device_bound.setter
    def is_hardware_device_bound(self, value):
        self._is_hardware_device_bound = value
    @property
    def sleepdata_list(self):
        return self._sleepdata_list

    @sleepdata_list.setter
    def sleepdata_list(self, value):
        if isinstance(value, list):
            self._sleepdata_list = list()
            for i in value:
                if isinstance(i, MedicalHmDailySleepRecord):
                    self._sleepdata_list.append(i)
                else:
                    self._sleepdata_list.append(MedicalHmDailySleepRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmSleepdataBatchqueryResponse, self).parse_response_content(response_content)
        if 'is_hardware_device_bound' in response:
            self.is_hardware_device_bound = response['is_hardware_device_bound']
        if 'sleepdata_list' in response:
            self.sleepdata_list = response['sleepdata_list']
