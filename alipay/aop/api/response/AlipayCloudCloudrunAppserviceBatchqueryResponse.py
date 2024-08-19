#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenapiServerDTO import OpenapiServerDTO


class AlipayCloudCloudrunAppserviceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunAppserviceBatchqueryResponse, self).__init__()
        self._server_list = None

    @property
    def server_list(self):
        return self._server_list

    @server_list.setter
    def server_list(self, value):
        if isinstance(value, list):
            self._server_list = list()
            for i in value:
                if isinstance(i, OpenapiServerDTO):
                    self._server_list.append(i)
                else:
                    self._server_list.append(OpenapiServerDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunAppserviceBatchqueryResponse, self).parse_response_content(response_content)
        if 'server_list' in response:
            self.server_list = response['server_list']
