#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleCharityProjectDTO import RecycleCharityProjectDTO


class AlipayCommerceRecycleCharityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleCharityQueryResponse, self).__init__()
        self._charity_project_list = None

    @property
    def charity_project_list(self):
        return self._charity_project_list

    @charity_project_list.setter
    def charity_project_list(self, value):
        if isinstance(value, list):
            self._charity_project_list = list()
            for i in value:
                if isinstance(i, RecycleCharityProjectDTO):
                    self._charity_project_list.append(i)
                else:
                    self._charity_project_list.append(RecycleCharityProjectDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleCharityQueryResponse, self).parse_response_content(response_content)
        if 'charity_project_list' in response:
            self.charity_project_list = response['charity_project_list']
