#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniMorphoAppCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMorphoAppCreateResponse, self).__init__()
        self._id = None
        self._mini_app_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMorphoAppCreateResponse, self).parse_response_content(response_content)
        if 'id' in response:
            self.id = response['id']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
