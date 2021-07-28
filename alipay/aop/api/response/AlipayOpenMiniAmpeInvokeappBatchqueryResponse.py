#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvokeAppInfo import InvokeAppInfo


class AlipayOpenMiniAmpeInvokeappBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeInvokeappBatchqueryResponse, self).__init__()
        self._invoke_app_list = None

    @property
    def invoke_app_list(self):
        return self._invoke_app_list

    @invoke_app_list.setter
    def invoke_app_list(self, value):
        if isinstance(value, list):
            self._invoke_app_list = list()
            for i in value:
                if isinstance(i, InvokeAppInfo):
                    self._invoke_app_list.append(i)
                else:
                    self._invoke_app_list.append(InvokeAppInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeInvokeappBatchqueryResponse, self).parse_response_content(response_content)
        if 'invoke_app_list' in response:
            self.invoke_app_list = response['invoke_app_list']
