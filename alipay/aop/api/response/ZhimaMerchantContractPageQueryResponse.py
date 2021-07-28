#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZmContractDetail import ZmContractDetail


class ZhimaMerchantContractPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantContractPageQueryResponse, self).__init__()
        self._biz_data = None
        self._biz_desc = None
        self._biz_result = None
        self._has_next = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, list):
            self._biz_data = list()
            for i in value:
                if isinstance(i, ZmContractDetail):
                    self._biz_data.append(i)
                else:
                    self._biz_data.append(ZmContractDetail.from_alipay_dict(i))
    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        self._biz_result = value
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantContractPageQueryResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'biz_desc' in response:
            self.biz_desc = response['biz_desc']
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
        if 'has_next' in response:
            self.has_next = response['has_next']
