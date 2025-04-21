#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduManagerInfo import EduManagerInfo


class AlipayCommerceEducateManagerDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateManagerDetailQueryResponse, self).__init__()
        self._manager_info = None

    @property
    def manager_info(self):
        return self._manager_info

    @manager_info.setter
    def manager_info(self, value):
        if isinstance(value, EduManagerInfo):
            self._manager_info = value
        else:
            self._manager_info = EduManagerInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateManagerDetailQueryResponse, self).parse_response_content(response_content)
        if 'manager_info' in response:
            self.manager_info = response['manager_info']
