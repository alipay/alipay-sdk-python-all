#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LmDivisionVO import LmDivisionVO


class AlipayCloudCloudpromoMallDivisionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallDivisionQueryResponse, self).__init__()
        self._division_list = None

    @property
    def division_list(self):
        return self._division_list

    @division_list.setter
    def division_list(self, value):
        if isinstance(value, list):
            self._division_list = list()
            for i in value:
                if isinstance(i, LmDivisionVO):
                    self._division_list.append(i)
                else:
                    self._division_list.append(LmDivisionVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallDivisionQueryResponse, self).parse_response_content(response_content)
        if 'division_list' in response:
            self.division_list = response['division_list']
