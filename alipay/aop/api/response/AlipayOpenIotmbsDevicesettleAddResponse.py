#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceSettleApplicantResult import DeviceSettleApplicantResult


class AlipayOpenIotmbsDevicesettleAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsDevicesettleAddResponse, self).__init__()
        self._orderStr = None
        self._settle_results = None

    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value
    @property
    def settle_results(self):
        return self._settle_results

    @settle_results.setter
    def settle_results(self, value):
        if isinstance(value, list):
            self._settle_results = list()
            for i in value:
                if isinstance(i, DeviceSettleApplicantResult):
                    self._settle_results.append(i)
                else:
                    self._settle_results.append(DeviceSettleApplicantResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsDevicesettleAddResponse, self).parse_response_content(response_content)
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
        if 'settle_results' in response:
            self.settle_results = response['settle_results']
