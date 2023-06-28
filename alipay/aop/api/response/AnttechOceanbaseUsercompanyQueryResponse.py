#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserCompanyDTO import UserCompanyDTO


class AnttechOceanbaseUsercompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUsercompanyQueryResponse, self).__init__()
        self._user_company_list = None

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

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseUsercompanyQueryResponse, self).parse_response_content(response_content)
        if 'user_company_list' in response:
            self.user_company_list = response['user_company_list']
