#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenValue import OpenValue


class AlipayOpenAppOpenidOpenidtounionidBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenidOpenidtounionidBatchqueryResponse, self).__init__()
        self._illegal_open_id_list = None
        self._unionid_list = None

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
    def unionid_list(self):
        return self._unionid_list

    @unionid_list.setter
    def unionid_list(self, value):
        if isinstance(value, list):
            self._unionid_list = list()
            for i in value:
                if isinstance(i, OpenValue):
                    self._unionid_list.append(i)
                else:
                    self._unionid_list.append(OpenValue.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenidOpenidtounionidBatchqueryResponse, self).parse_response_content(response_content)
        if 'illegal_open_id_list' in response:
            self.illegal_open_id_list = response['illegal_open_id_list']
        if 'unionid_list' in response:
            self.unionid_list = response['unionid_list']
