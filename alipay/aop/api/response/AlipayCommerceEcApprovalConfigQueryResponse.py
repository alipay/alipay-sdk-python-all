#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApprovalConfigDTO import ApprovalConfigDTO


class AlipayCommerceEcApprovalConfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcApprovalConfigQueryResponse, self).__init__()
        self._config_list = None

    @property
    def config_list(self):
        return self._config_list

    @config_list.setter
    def config_list(self, value):
        if isinstance(value, list):
            self._config_list = list()
            for i in value:
                if isinstance(i, ApprovalConfigDTO):
                    self._config_list.append(i)
                else:
                    self._config_list.append(ApprovalConfigDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcApprovalConfigQueryResponse, self).parse_response_content(response_content)
        if 'config_list' in response:
            self.config_list = response['config_list']
