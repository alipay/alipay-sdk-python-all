#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SimpleOpenApiPrivilegeDetail import SimpleOpenApiPrivilegeDetail


class AlipayUserPrivilegeSkillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPrivilegeSkillQueryResponse, self).__init__()
        self._simple_open_api_privilege_detail_list = None

    @property
    def simple_open_api_privilege_detail_list(self):
        return self._simple_open_api_privilege_detail_list

    @simple_open_api_privilege_detail_list.setter
    def simple_open_api_privilege_detail_list(self, value):
        if isinstance(value, list):
            self._simple_open_api_privilege_detail_list = list()
            for i in value:
                if isinstance(i, SimpleOpenApiPrivilegeDetail):
                    self._simple_open_api_privilege_detail_list.append(i)
                else:
                    self._simple_open_api_privilege_detail_list.append(SimpleOpenApiPrivilegeDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserPrivilegeSkillQueryResponse, self).parse_response_content(response_content)
        if 'simple_open_api_privilege_detail_list' in response:
            self.simple_open_api_privilege_detail_list = response['simple_open_api_privilege_detail_list']
