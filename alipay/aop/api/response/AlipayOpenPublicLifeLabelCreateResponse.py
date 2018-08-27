#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeLabelCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeLabelCreateResponse, self).__init__()
        self._label_id = None

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeLabelCreateResponse, self).parse_response_content(response_content)
        if 'label_id' in response:
            self.label_id = response['label_id']
