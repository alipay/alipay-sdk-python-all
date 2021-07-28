#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BPaaSServiceInfo import BPaaSServiceInfo


class AlipayOpenBpaasServiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenBpaasServiceQueryResponse, self).__init__()
        self._service_list = None

    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, BPaaSServiceInfo):
                    self._service_list.append(i)
                else:
                    self._service_list.append(BPaaSServiceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenBpaasServiceQueryResponse, self).parse_response_content(response_content)
        if 'service_list' in response:
            self.service_list = response['service_list']
