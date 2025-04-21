#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoapInfoDTO import PoapInfoDTO


class AnttechNftPoapTenantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftPoapTenantQueryResponse, self).__init__()
        self._has_next = None
        self._medal_list = None
        self._total = None

    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def medal_list(self):
        return self._medal_list

    @medal_list.setter
    def medal_list(self, value):
        if isinstance(value, list):
            self._medal_list = list()
            for i in value:
                if isinstance(i, PoapInfoDTO):
                    self._medal_list.append(i)
                else:
                    self._medal_list.append(PoapInfoDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftPoapTenantQueryResponse, self).parse_response_content(response_content)
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'medal_list' in response:
            self.medal_list = response['medal_list']
        if 'total' in response:
            self.total = response['total']
