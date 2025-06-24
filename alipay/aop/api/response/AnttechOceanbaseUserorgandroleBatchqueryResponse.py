#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserOrgAndRoleDTO import UserOrgAndRoleDTO


class AnttechOceanbaseUserorgandroleBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUserorgandroleBatchqueryResponse, self).__init__()
        self._user_org_and_role_list = None

    @property
    def user_org_and_role_list(self):
        return self._user_org_and_role_list

    @user_org_and_role_list.setter
    def user_org_and_role_list(self, value):
        if isinstance(value, list):
            self._user_org_and_role_list = list()
            for i in value:
                if isinstance(i, UserOrgAndRoleDTO):
                    self._user_org_and_role_list.append(i)
                else:
                    self._user_org_and_role_list.append(UserOrgAndRoleDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseUserorgandroleBatchqueryResponse, self).parse_response_content(response_content)
        if 'user_org_and_role_list' in response:
            self.user_org_and_role_list = response['user_org_and_role_list']
