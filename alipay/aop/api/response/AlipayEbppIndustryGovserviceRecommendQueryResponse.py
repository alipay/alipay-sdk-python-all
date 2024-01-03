#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceDetailInfo import ServiceDetailInfo


class AlipayEbppIndustryGovserviceRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryGovserviceRecommendQueryResponse, self).__init__()
        self._recommend_service = None

    @property
    def recommend_service(self):
        return self._recommend_service

    @recommend_service.setter
    def recommend_service(self, value):
        if isinstance(value, list):
            self._recommend_service = list()
            for i in value:
                if isinstance(i, ServiceDetailInfo):
                    self._recommend_service.append(i)
                else:
                    self._recommend_service.append(ServiceDetailInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryGovserviceRecommendQueryResponse, self).parse_response_content(response_content)
        if 'recommend_service' in response:
            self.recommend_service = response['recommend_service']
