#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BailAuthOrderDTO import BailAuthOrderDTO
from alipay.aop.api.domain.StandardBailDTO import StandardBailDTO


class AlipayFundBailOrderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBailOrderBatchqueryResponse, self).__init__()
        self._bail_auth_list = None
        self._standard_bail_list = None

    @property
    def bail_auth_list(self):
        return self._bail_auth_list

    @bail_auth_list.setter
    def bail_auth_list(self, value):
        if isinstance(value, list):
            self._bail_auth_list = list()
            for i in value:
                if isinstance(i, BailAuthOrderDTO):
                    self._bail_auth_list.append(i)
                else:
                    self._bail_auth_list.append(BailAuthOrderDTO.from_alipay_dict(i))
    @property
    def standard_bail_list(self):
        return self._standard_bail_list

    @standard_bail_list.setter
    def standard_bail_list(self, value):
        if isinstance(value, list):
            self._standard_bail_list = list()
            for i in value:
                if isinstance(i, StandardBailDTO):
                    self._standard_bail_list.append(i)
                else:
                    self._standard_bail_list.append(StandardBailDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundBailOrderBatchqueryResponse, self).parse_response_content(response_content)
        if 'bail_auth_list' in response:
            self.bail_auth_list = response['bail_auth_list']
        if 'standard_bail_list' in response:
            self.standard_bail_list = response['standard_bail_list']
