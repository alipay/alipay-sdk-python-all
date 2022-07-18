#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasPutplanCreateResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasPutplanCreateResponse, self).__init__()
        self._put_plan_id = None

    @property
    def put_plan_id(self):
        return self._put_plan_id

    @put_plan_id.setter
    def put_plan_id(self, value):
        self._put_plan_id = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasPutplanCreateResponse, self).parse_response_content(response_content)
        if 'put_plan_id' in response:
            self.put_plan_id = response['put_plan_id']
