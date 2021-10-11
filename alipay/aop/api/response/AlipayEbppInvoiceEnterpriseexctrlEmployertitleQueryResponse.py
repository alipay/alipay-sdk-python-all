#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseTitleInfo import EnterpriseTitleInfo


class AlipayEbppInvoiceEnterpriseexctrlEmployertitleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseexctrlEmployertitleQueryResponse, self).__init__()
        self._code = None
        self._msg = None
        self._title_info = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def title_info(self):
        return self._title_info

    @title_info.setter
    def title_info(self, value):
        if isinstance(value, EnterpriseTitleInfo):
            self._title_info = value
        else:
            self._title_info = EnterpriseTitleInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseexctrlEmployertitleQueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'title_info' in response:
            self.title_info = response['title_info']
