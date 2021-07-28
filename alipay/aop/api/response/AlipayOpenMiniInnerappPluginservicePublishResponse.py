#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerappPluginservicePublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerappPluginservicePublishResponse, self).__init__()
        self._ability_id = None

    @property
    def ability_id(self):
        return self._ability_id

    @ability_id.setter
    def ability_id(self, value):
        self._ability_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerappPluginservicePublishResponse, self).parse_response_content(response_content)
        if 'ability_id' in response:
            self.ability_id = response['ability_id']
