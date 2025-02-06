#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceSearchDetailInfo import ServiceSearchDetailInfo


class AlipayEbppIndustryGovserviceSearchRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryGovserviceSearchRecommendResponse, self).__init__()
        self._search_service_list = None

    @property
    def search_service_list(self):
        return self._search_service_list

    @search_service_list.setter
    def search_service_list(self, value):
        if isinstance(value, list):
            self._search_service_list = list()
            for i in value:
                if isinstance(i, ServiceSearchDetailInfo):
                    self._search_service_list.append(i)
                else:
                    self._search_service_list.append(ServiceSearchDetailInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryGovserviceSearchRecommendResponse, self).parse_response_content(response_content)
        if 'search_service_list' in response:
            self.search_service_list = response['search_service_list']
