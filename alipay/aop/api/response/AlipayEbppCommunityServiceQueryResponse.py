#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommunityServiceInfo import CommunityServiceInfo


class AlipayEbppCommunityServiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityServiceQueryResponse, self).__init__()
        self._service_info_list = None

    @property
    def service_info_list(self):
        return self._service_info_list

    @service_info_list.setter
    def service_info_list(self, value):
        if isinstance(value, list):
            self._service_info_list = list()
            for i in value:
                if isinstance(i, CommunityServiceInfo):
                    self._service_info_list.append(i)
                else:
                    self._service_info_list.append(CommunityServiceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityServiceQueryResponse, self).parse_response_content(response_content)
        if 'service_info_list' in response:
            self.service_info_list = response['service_info_list']
