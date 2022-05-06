#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrgRoleDTO import OrgRoleDTO


class AlipayBossBaseAntauthorizeOrgroleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseAntauthorizeOrgroleQueryResponse, self).__init__()
        self._org_role = None

    @property
    def org_role(self):
        return self._org_role

    @org_role.setter
    def org_role(self, value):
        if isinstance(value, OrgRoleDTO):
            self._org_role = value
        else:
            self._org_role = OrgRoleDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseAntauthorizeOrgroleQueryResponse, self).parse_response_content(response_content)
        if 'org_role' in response:
            self.org_role = response['org_role']
