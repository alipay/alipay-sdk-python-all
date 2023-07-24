#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenIdValue import OpenIdValue


class AlipayOpenAppOpenidOpenidtouidBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenidOpenidtouidBatchqueryResponse, self).__init__()
        self._illegal_open_id_list = None
        self._uid_list = None

    @property
    def illegal_open_id_list(self):
        return self._illegal_open_id_list

    @illegal_open_id_list.setter
    def illegal_open_id_list(self, value):
        if isinstance(value, list):
            self._illegal_open_id_list = list()
            for i in value:
                self._illegal_open_id_list.append(i)
    @property
    def uid_list(self):
        return self._uid_list

    @uid_list.setter
    def uid_list(self, value):
        if isinstance(value, list):
            self._uid_list = list()
            for i in value:
                if isinstance(i, OpenIdValue):
                    self._uid_list.append(i)
                else:
                    self._uid_list.append(OpenIdValue.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenidOpenidtouidBatchqueryResponse, self).parse_response_content(response_content)
        if 'illegal_open_id_list' in response:
            self.illegal_open_id_list = response['illegal_open_id_list']
        if 'uid_list' in response:
            self.uid_list = response['uid_list']
