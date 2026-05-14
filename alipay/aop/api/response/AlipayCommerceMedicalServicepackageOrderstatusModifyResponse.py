#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServicepackageOrderstatusModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageOrderstatusModifyResponse, self).__init__()
        self._operate_res = None

    @property
    def operate_res(self):
        return self._operate_res

    @operate_res.setter
    def operate_res(self, value):
        self._operate_res = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageOrderstatusModifyResponse, self).parse_response_content(response_content)
        if 'operate_res' in response:
            self.operate_res = response['operate_res']
