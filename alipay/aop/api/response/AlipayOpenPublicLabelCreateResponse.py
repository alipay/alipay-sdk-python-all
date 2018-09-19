#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLabelCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLabelCreateResponse, self).__init__()
        self._id = None
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLabelCreateResponse, self).parse_response_content(response_content)
        if 'id' in response:
            self.id = response['id']
        if 'name' in response:
            self.name = response['name']
