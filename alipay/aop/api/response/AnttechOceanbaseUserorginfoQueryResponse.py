#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserInfoDetailDTO import UserInfoDetailDTO
from alipay.aop.api.domain.UserOrganizationDTO import UserOrganizationDTO


class AnttechOceanbaseUserorginfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUserorginfoQueryResponse, self).__init__()
        self._basic_info = None
        self._org_info_list = None

    @property
    def basic_info(self):
        return self._basic_info

    @basic_info.setter
    def basic_info(self, value):
        if isinstance(value, UserInfoDetailDTO):
            self._basic_info = value
        else:
            self._basic_info = UserInfoDetailDTO.from_alipay_dict(value)
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
        response = super(AnttechOceanbaseUserorginfoQueryResponse, self).parse_response_content(response_content)
        if 'basic_info' in response:
            self.basic_info = response['basic_info']
        if 'org_info_list' in response:
            self.org_info_list = response['org_info_list']
