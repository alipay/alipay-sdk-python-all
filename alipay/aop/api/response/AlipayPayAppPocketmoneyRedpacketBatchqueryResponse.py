#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RedPocketInfo import RedPocketInfo


class AlipayPayAppPocketmoneyRedpacketBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppPocketmoneyRedpacketBatchqueryResponse, self).__init__()
        self._red_pocket_list = None

    @property
    def red_pocket_list(self):
        return self._red_pocket_list

    @red_pocket_list.setter
    def red_pocket_list(self, value):
        if isinstance(value, list):
            self._red_pocket_list = list()
            for i in value:
                if isinstance(i, RedPocketInfo):
                    self._red_pocket_list.append(i)
                else:
                    self._red_pocket_list.append(RedPocketInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppPocketmoneyRedpacketBatchqueryResponse, self).parse_response_content(response_content)
        if 'red_pocket_list' in response:
            self.red_pocket_list = response['red_pocket_list']
