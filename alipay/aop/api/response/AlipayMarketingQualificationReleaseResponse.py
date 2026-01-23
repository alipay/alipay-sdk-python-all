#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingQualificationReleaseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQualificationReleaseResponse, self).__init__()
        self._qual_id = None
        self._qual_instance_id = None

    @property
    def qual_id(self):
        return self._qual_id

    @qual_id.setter
    def qual_id(self, value):
        self._qual_id = value
    @property
    def qual_instance_id(self):
        return self._qual_instance_id

    @qual_instance_id.setter
    def qual_instance_id(self, value):
        self._qual_instance_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQualificationReleaseResponse, self).parse_response_content(response_content)
        if 'qual_id' in response:
            self.qual_id = response['qual_id']
        if 'qual_instance_id' in response:
            self.qual_instance_id = response['qual_instance_id']
