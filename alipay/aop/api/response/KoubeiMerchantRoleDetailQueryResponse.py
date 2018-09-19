#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessPermission import BusinessPermission


class KoubeiMerchantRoleDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantRoleDetailQueryResponse, self).__init__()
        self._permissions = None
        self._role_code = None
        self._role_id = None
        self._role_name = None

    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        if isinstance(value, list):
            self._permissions = list()
            for i in value:
                if isinstance(i, BusinessPermission):
                    self._permissions.append(i)
                else:
                    self._permissions.append(BusinessPermission.from_alipay_dict(i))
    @property
    def role_code(self):
        return self._role_code

    @role_code.setter
    def role_code(self, value):
        self._role_code = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantRoleDetailQueryResponse, self).parse_response_content(response_content)
        if 'permissions' in response:
            self.permissions = response['permissions']
        if 'role_code' in response:
            self.role_code = response['role_code']
        if 'role_id' in response:
            self.role_id = response['role_id']
        if 'role_name' in response:
            self.role_name = response['role_name']
