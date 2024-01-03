#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrgRoleDTO import OrgRoleDTO


class AlipayBossBaseAntauthorizeRoleuserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseAntauthorizeRoleuserQueryResponse, self).__init__()
        self._role_user_list = None

    @property
    def role_user_list(self):
        return self._role_user_list

    @role_user_list.setter
    def role_user_list(self, value):
        if isinstance(value, list):
            self._role_user_list = list()
            for i in value:
                if isinstance(i, OrgRoleDTO):
                    self._role_user_list.append(i)
                else:
                    self._role_user_list.append(OrgRoleDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseAntauthorizeRoleuserQueryResponse, self).parse_response_content(response_content)
        if 'role_user_list' in response:
            self.role_user_list = response['role_user_list']
