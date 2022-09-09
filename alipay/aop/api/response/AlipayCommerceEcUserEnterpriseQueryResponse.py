#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseInfoDTO import EnterpriseInfoDTO


class AlipayCommerceEcUserEnterpriseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcUserEnterpriseQueryResponse, self).__init__()
        self._enterprise_info_list = None

    @property
    def enterprise_info_list(self):
        return self._enterprise_info_list

    @enterprise_info_list.setter
    def enterprise_info_list(self, value):
        if isinstance(value, list):
            self._enterprise_info_list = list()
            for i in value:
                if isinstance(i, EnterpriseInfoDTO):
                    self._enterprise_info_list.append(i)
                else:
                    self._enterprise_info_list.append(EnterpriseInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcUserEnterpriseQueryResponse, self).parse_response_content(response_content)
        if 'enterprise_info_list' in response:
            self.enterprise_info_list = response['enterprise_info_list']
