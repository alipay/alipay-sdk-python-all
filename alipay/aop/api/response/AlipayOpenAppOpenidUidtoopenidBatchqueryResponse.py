#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenIdValue import OpenIdValue


class AlipayOpenAppOpenidUidtoopenidBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenidUidtoopenidBatchqueryResponse, self).__init__()
        self._open_id_list = None

    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                if isinstance(i, OpenIdValue):
                    self._open_id_list.append(i)
                else:
                    self._open_id_list.append(OpenIdValue.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenidUidtoopenidBatchqueryResponse, self).parse_response_content(response_content)
        if 'open_id_list' in response:
            self.open_id_list = response['open_id_list']
