#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbadvertRoleInfoResponse import KbadvertRoleInfoResponse


class KoubeiAdvertCommissionRoleQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionRoleQueryResponse, self).__init__()
        self._role_infos = None

    @property
    def role_infos(self):
        return self._role_infos

    @role_infos.setter
    def role_infos(self, value):
        if isinstance(value, list):
            self._role_infos = list()
            for i in value:
                if isinstance(i, KbadvertRoleInfoResponse):
                    self._role_infos.append(i)
                else:
                    self._role_infos.append(KbadvertRoleInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionRoleQueryResponse, self).parse_response_content(response_content)
        if 'role_infos' in response:
            self.role_infos = response['role_infos']
