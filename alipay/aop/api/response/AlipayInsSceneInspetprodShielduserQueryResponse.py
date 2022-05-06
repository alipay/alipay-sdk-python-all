#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInspetprodShielduserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInspetprodShielduserQueryResponse, self).__init__()
        self._shield_wx_title = None
        self._shield_wx_url = None

    @property
    def shield_wx_title(self):
        return self._shield_wx_title

    @shield_wx_title.setter
    def shield_wx_title(self, value):
        self._shield_wx_title = value
    @property
    def shield_wx_url(self):
        return self._shield_wx_url

    @shield_wx_url.setter
    def shield_wx_url(self, value):
        self._shield_wx_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInspetprodShielduserQueryResponse, self).parse_response_content(response_content)
        if 'shield_wx_title' in response:
            self.shield_wx_title = response['shield_wx_title']
        if 'shield_wx_url' in response:
            self.shield_wx_url = response['shield_wx_url']
