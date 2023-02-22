#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessDistrictInfo import BusinessDistrictInfo


class AlipayOpenSearchboxBusinessdistrictQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchboxBusinessdistrictQueryResponse, self).__init__()
        self._business_district_info_list = None

    @property
    def business_district_info_list(self):
        return self._business_district_info_list

    @business_district_info_list.setter
    def business_district_info_list(self, value):
        if isinstance(value, list):
            self._business_district_info_list = list()
            for i in value:
                if isinstance(i, BusinessDistrictInfo):
                    self._business_district_info_list.append(i)
                else:
                    self._business_district_info_list.append(BusinessDistrictInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchboxBusinessdistrictQueryResponse, self).parse_response_content(response_content)
        if 'business_district_info_list' in response:
            self.business_district_info_list = response['business_district_info_list']
