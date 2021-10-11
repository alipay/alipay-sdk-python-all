#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseTitleInfo import EnterpriseTitleInfo


class AlipayEbppInvoiceEnterpriseexctrlEmployertitleBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseexctrlEmployertitleBatchqueryResponse, self).__init__()
        self._code = None
        self._msg = None
        self._title_info_list = None

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
    def title_info_list(self):
        return self._title_info_list

    @title_info_list.setter
    def title_info_list(self, value):
        if isinstance(value, list):
            self._title_info_list = list()
            for i in value:
                if isinstance(i, EnterpriseTitleInfo):
                    self._title_info_list.append(i)
                else:
                    self._title_info_list.append(EnterpriseTitleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseexctrlEmployertitleBatchqueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'title_info_list' in response:
            self.title_info_list = response['title_info_list']
