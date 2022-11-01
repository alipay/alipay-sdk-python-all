#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgriRegionInfo import AgriRegionInfo


class AnttechBlockchainDefinDataserviceRegioninfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceRegioninfoQueryResponse, self).__init__()
        self._region_list = None

    @property
    def region_list(self):
        return self._region_list

    @region_list.setter
    def region_list(self, value):
        if isinstance(value, list):
            self._region_list = list()
            for i in value:
                if isinstance(i, AgriRegionInfo):
                    self._region_list.append(i)
                else:
                    self._region_list.append(AgriRegionInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceRegioninfoQueryResponse, self).parse_response_content(response_content)
        if 'region_list' in response:
            self.region_list = response['region_list']
