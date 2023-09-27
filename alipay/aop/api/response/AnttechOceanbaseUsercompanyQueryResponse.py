#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserCompanyDTO import UserCompanyDTO
from alipay.aop.api.domain.UserOrganizationDTO import UserOrganizationDTO


class AnttechOceanbaseUsercompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUsercompanyQueryResponse, self).__init__()
        self._user_company_list = None
        self._user_organization_list = None

    @property
    def user_company_list(self):
        return self._user_company_list

    @user_company_list.setter
    def user_company_list(self, value):
        if isinstance(value, list):
            self._user_company_list = list()
            for i in value:
                if isinstance(i, UserCompanyDTO):
                    self._user_company_list.append(i)
                else:
                    self._user_company_list.append(UserCompanyDTO.from_alipay_dict(i))
    @property
    def user_organization_list(self):
        return self._user_organization_list

    @user_organization_list.setter
    def user_organization_list(self, value):
        if isinstance(value, list):
            self._user_organization_list = list()
            for i in value:
                if isinstance(i, UserOrganizationDTO):
                    self._user_organization_list.append(i)
                else:
                    self._user_organization_list.append(UserOrganizationDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseUsercompanyQueryResponse, self).parse_response_content(response_content)
        if 'user_company_list' in response:
            self.user_company_list = response['user_company_list']
        if 'user_organization_list' in response:
            self.user_organization_list = response['user_organization_list']
