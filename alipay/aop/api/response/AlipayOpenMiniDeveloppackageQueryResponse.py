#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SingleStartAppVO import SingleStartAppVO


class AlipayOpenMiniDeveloppackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDeveloppackageQueryResponse, self).__init__()
        self._single_start_app_vo = None

    @property
    def single_start_app_vo(self):
        return self._single_start_app_vo

    @single_start_app_vo.setter
    def single_start_app_vo(self, value):
        if isinstance(value, SingleStartAppVO):
            self._single_start_app_vo = value
        else:
            self._single_start_app_vo = SingleStartAppVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDeveloppackageQueryResponse, self).parse_response_content(response_content)
        if 'single_start_app_vo' in response:
            self.single_start_app_vo = response['single_start_app_vo']
