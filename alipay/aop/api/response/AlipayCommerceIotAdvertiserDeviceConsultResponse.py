#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceRelationData import DeviceRelationData


class AlipayCommerceIotAdvertiserDeviceConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserDeviceConsultResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, DeviceRelationData):
                    self._result.append(i)
                else:
                    self._result.append(DeviceRelationData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserDeviceConsultResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
