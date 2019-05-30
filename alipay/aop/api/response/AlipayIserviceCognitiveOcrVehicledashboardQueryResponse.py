#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehicleDashboardResult import VehicleDashboardResult


class AlipayIserviceCognitiveOcrVehicledashboardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrVehicledashboardQueryResponse, self).__init__()
        self._ip = None
        self._result = None
        self._ret = None
        self._rt = None
        self._sid = None

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, VehicleDashboardResult):
                    self._result.append(i)
                else:
                    self._result.append(VehicleDashboardResult.from_alipay_dict(i))
    @property
    def ret(self):
        return self._ret

    @ret.setter
    def ret(self, value):
        self._ret = value
    @property
    def rt(self):
        return self._rt

    @rt.setter
    def rt(self, value):
        self._rt = value
    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        self._sid = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrVehicledashboardQueryResponse, self).parse_response_content(response_content)
        if 'ip' in response:
            self.ip = response['ip']
        if 'result' in response:
            self.result = response['result']
        if 'ret' in response:
            self.ret = response['ret']
        if 'rt' in response:
            self.rt = response['rt']
        if 'sid' in response:
            self.sid = response['sid']
