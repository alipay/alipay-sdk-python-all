#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BindApplyResult import BindApplyResult
from alipay.aop.api.domain.IotDeviceBindBaseInfo import IotDeviceBindBaseInfo


class AlipayOfflineProviderCollaborateDevicebindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateDevicebindQueryResponse, self).__init__()
        self._apply_result_info = None
        self._bind_info = None

    @property
    def apply_result_info(self):
        return self._apply_result_info

    @apply_result_info.setter
    def apply_result_info(self, value):
        if isinstance(value, list):
            self._apply_result_info = list()
            for i in value:
                if isinstance(i, BindApplyResult):
                    self._apply_result_info.append(i)
                else:
                    self._apply_result_info.append(BindApplyResult.from_alipay_dict(i))
    @property
    def bind_info(self):
        return self._bind_info

    @bind_info.setter
    def bind_info(self, value):
        if isinstance(value, IotDeviceBindBaseInfo):
            self._bind_info = value
        else:
            self._bind_info = IotDeviceBindBaseInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateDevicebindQueryResponse, self).parse_response_content(response_content)
        if 'apply_result_info' in response:
            self.apply_result_info = response['apply_result_info']
        if 'bind_info' in response:
            self.bind_info = response['bind_info']
