#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInspetprodSubscribeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInspetprodSubscribeQueryResponse, self).__init__()
        self._subscribe = None

    @property
    def subscribe(self):
        return self._subscribe

    @subscribe.setter
    def subscribe(self, value):
        self._subscribe = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInspetprodSubscribeQueryResponse, self).parse_response_content(response_content)
        if 'subscribe' in response:
            self.subscribe = response['subscribe']
