#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourceDataVO import ResourceDataVO


class AlipayOpenMiniResourceDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniResourceDataQueryResponse, self).__init__()
        self._resource_data_list = None

    @property
    def resource_data_list(self):
        return self._resource_data_list

    @resource_data_list.setter
    def resource_data_list(self, value):
        if isinstance(value, list):
            self._resource_data_list = list()
            for i in value:
                if isinstance(i, ResourceDataVO):
                    self._resource_data_list.append(i)
                else:
                    self._resource_data_list.append(ResourceDataVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniResourceDataQueryResponse, self).parse_response_content(response_content)
        if 'resource_data_list' in response:
            self.resource_data_list = response['resource_data_list']
