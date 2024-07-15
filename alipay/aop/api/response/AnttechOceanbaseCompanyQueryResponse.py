#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserOrganizationDTO import UserOrganizationDTO


class AnttechOceanbaseCompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseCompanyQueryResponse, self).__init__()
        self._org_info_list = None

    @property
    def org_info_list(self):
        return self._org_info_list

    @org_info_list.setter
    def org_info_list(self, value):
        if isinstance(value, list):
            self._org_info_list = list()
            for i in value:
                if isinstance(i, UserOrganizationDTO):
                    self._org_info_list.append(i)
                else:
                    self._org_info_list.append(UserOrganizationDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseCompanyQueryResponse, self).parse_response_content(response_content)
        if 'org_info_list' in response:
            self.org_info_list = response['org_info_list']
