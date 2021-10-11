#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AllocDetailDTO import AllocDetailDTO


class AlipayFundJointaccountFundallocListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountFundallocListQueryResponse, self).__init__()
        self._alloc_detail_list = None
        self._last_id = None

    @property
    def alloc_detail_list(self):
        return self._alloc_detail_list

    @alloc_detail_list.setter
    def alloc_detail_list(self, value):
        if isinstance(value, list):
            self._alloc_detail_list = list()
            for i in value:
                if isinstance(i, AllocDetailDTO):
                    self._alloc_detail_list.append(i)
                else:
                    self._alloc_detail_list.append(AllocDetailDTO.from_alipay_dict(i))
    @property
    def last_id(self):
        return self._last_id

    @last_id.setter
    def last_id(self, value):
        self._last_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountFundallocListQueryResponse, self).parse_response_content(response_content)
        if 'alloc_detail_list' in response:
            self.alloc_detail_list = response['alloc_detail_list']
        if 'last_id' in response:
            self.last_id = response['last_id']
