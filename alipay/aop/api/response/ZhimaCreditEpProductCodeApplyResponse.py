#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CodeResInfo import CodeResInfo


class ZhimaCreditEpProductCodeApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpProductCodeApplyResponse, self).__init__()
        self._apply_no = None
        self._code_list = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def code_list(self):
        return self._code_list

    @code_list.setter
    def code_list(self, value):
        if isinstance(value, list):
            self._code_list = list()
            for i in value:
                if isinstance(i, CodeResInfo):
                    self._code_list.append(i)
                else:
                    self._code_list.append(CodeResInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpProductCodeApplyResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'code_list' in response:
            self.code_list = response['code_list']
