#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduRoleInfo import EduRoleInfo


class AlipayCommerceEducateRoleInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRoleInfoBatchqueryResponse, self).__init__()
        self._role_list = None
        self._total_num = None

    @property
    def role_list(self):
        return self._role_list

    @role_list.setter
    def role_list(self, value):
        if isinstance(value, list):
            self._role_list = list()
            for i in value:
                if isinstance(i, EduRoleInfo):
                    self._role_list.append(i)
                else:
                    self._role_list.append(EduRoleInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRoleInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'role_list' in response:
            self.role_list = response['role_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
