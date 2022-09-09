#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseInfoDTO import EnterpriseInfoDTO


class AlipayCommerceEcEnterpriseInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseInfoQueryResponse, self).__init__()
        self._enterprise_info = None

    @property
    def enterprise_info(self):
        return self._enterprise_info

    @enterprise_info.setter
    def enterprise_info(self, value):
        if isinstance(value, EnterpriseInfoDTO):
            self._enterprise_info = value
        else:
            self._enterprise_info = EnterpriseInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseInfoQueryResponse, self).parse_response_content(response_content)
        if 'enterprise_info' in response:
            self.enterprise_info = response['enterprise_info']
