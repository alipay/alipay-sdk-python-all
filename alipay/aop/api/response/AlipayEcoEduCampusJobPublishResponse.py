#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduCampusJobPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduCampusJobPublishResponse, self).__init__()
        self._content = None
        self._description = None
        self._isv_code = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduCampusJobPublishResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'description' in response:
            self.description = response['description']
        if 'isv_code' in response:
            self.isv_code = response['isv_code']
