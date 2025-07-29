#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsPointWorkCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsPointWorkCreateResponse, self).__init__()
        self._logistics_point_work_id = None

    @property
    def logistics_point_work_id(self):
        return self._logistics_point_work_id

    @logistics_point_work_id.setter
    def logistics_point_work_id(self, value):
        self._logistics_point_work_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsPointWorkCreateResponse, self).parse_response_content(response_content)
        if 'logistics_point_work_id' in response:
            self.logistics_point_work_id = response['logistics_point_work_id']
