#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenIdValue import OpenIdValue


class AlipayOpenAppOpenidBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenidBatchqueryResponse, self).__init__()
        self._illegal_user_id_list = None
        self._open_id_list = None

    @property
    def illegal_user_id_list(self):
        return self._illegal_user_id_list

    @illegal_user_id_list.setter
    def illegal_user_id_list(self, value):
        if isinstance(value, list):
            self._illegal_user_id_list = list()
            for i in value:
                self._illegal_user_id_list.append(i)
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
        response = super(AlipayOpenAppOpenidBatchqueryResponse, self).parse_response_content(response_content)
        if 'illegal_user_id_list' in response:
            self.illegal_user_id_list = response['illegal_user_id_list']
        if 'open_id_list' in response:
            self.open_id_list = response['open_id_list']
