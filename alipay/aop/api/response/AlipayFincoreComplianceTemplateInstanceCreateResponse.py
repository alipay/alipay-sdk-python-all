#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceTemplateInstanceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateInstanceCreateResponse, self).__init__()
        self._biz_instance_id = None

    @property
    def biz_instance_id(self):
        return self._biz_instance_id

    @biz_instance_id.setter
    def biz_instance_id(self, value):
        self._biz_instance_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateInstanceCreateResponse, self).parse_response_content(response_content)
        if 'biz_instance_id' in response:
            self.biz_instance_id = response['biz_instance_id']
