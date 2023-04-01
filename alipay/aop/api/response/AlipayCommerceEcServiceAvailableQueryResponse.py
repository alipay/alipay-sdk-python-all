#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceBaseInfo import ServiceBaseInfo


class AlipayCommerceEcServiceAvailableQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcServiceAvailableQueryResponse, self).__init__()
        self._service_base_info_list = None

    @property
    def service_base_info_list(self):
        return self._service_base_info_list

    @service_base_info_list.setter
    def service_base_info_list(self, value):
        if isinstance(value, list):
            self._service_base_info_list = list()
            for i in value:
                if isinstance(i, ServiceBaseInfo):
                    self._service_base_info_list.append(i)
                else:
                    self._service_base_info_list.append(ServiceBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcServiceAvailableQueryResponse, self).parse_response_content(response_content)
        if 'service_base_info_list' in response:
            self.service_base_info_list = response['service_base_info_list']
