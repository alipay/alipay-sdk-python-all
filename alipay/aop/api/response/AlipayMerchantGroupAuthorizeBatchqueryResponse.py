#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupAuthorizeVO import GroupAuthorizeVO


class AlipayMerchantGroupAuthorizeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAuthorizeBatchqueryResponse, self).__init__()
        self._authorize_info_list = None
        self._total_count = None

    @property
    def authorize_info_list(self):
        return self._authorize_info_list

    @authorize_info_list.setter
    def authorize_info_list(self, value):
        if isinstance(value, list):
            self._authorize_info_list = list()
            for i in value:
                if isinstance(i, GroupAuthorizeVO):
                    self._authorize_info_list.append(i)
                else:
                    self._authorize_info_list.append(GroupAuthorizeVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAuthorizeBatchqueryResponse, self).parse_response_content(response_content)
        if 'authorize_info_list' in response:
            self.authorize_info_list = response['authorize_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
