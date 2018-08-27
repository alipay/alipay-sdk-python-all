#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLabelUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLabelUserQueryResponse, self).__init__()
        self._label_ids = None

    @property
    def label_ids(self):
        return self._label_ids

    @label_ids.setter
    def label_ids(self, value):
        self._label_ids = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLabelUserQueryResponse, self).parse_response_content(response_content)
        if 'label_ids' in response:
            self.label_ids = response['label_ids']
