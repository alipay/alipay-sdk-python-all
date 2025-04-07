#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcEmployeeTitleFailed import EcEmployeeTitleFailed


class AlipayCommerceEcEmployeeTitleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeTitleCreateResponse, self).__init__()
        self._title_failed_list = None

    @property
    def title_failed_list(self):
        return self._title_failed_list

    @title_failed_list.setter
    def title_failed_list(self, value):
        if isinstance(value, EcEmployeeTitleFailed):
            self._title_failed_list = value
        else:
            self._title_failed_list = EcEmployeeTitleFailed.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeTitleCreateResponse, self).parse_response_content(response_content)
        if 'title_failed_list' in response:
            self.title_failed_list = response['title_failed_list']
