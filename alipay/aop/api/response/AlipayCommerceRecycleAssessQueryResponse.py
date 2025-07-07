#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleAssessDTO import RecycleAssessDTO


class AlipayCommerceRecycleAssessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleAssessQueryResponse, self).__init__()
        self._assess_info_list = None

    @property
    def assess_info_list(self):
        return self._assess_info_list

    @assess_info_list.setter
    def assess_info_list(self, value):
        if isinstance(value, list):
            self._assess_info_list = list()
            for i in value:
                if isinstance(i, RecycleAssessDTO):
                    self._assess_info_list.append(i)
                else:
                    self._assess_info_list.append(RecycleAssessDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleAssessQueryResponse, self).parse_response_content(response_content)
        if 'assess_info_list' in response:
            self.assess_info_list = response['assess_info_list']
