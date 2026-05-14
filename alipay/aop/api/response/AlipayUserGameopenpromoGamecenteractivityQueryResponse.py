#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGameopenpromoGamecenteractivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGameopenpromoGamecenteractivityQueryResponse, self).__init__()
        self._activity_icon_url = None
        self._activity_jump_link = None

    @property
    def activity_icon_url(self):
        return self._activity_icon_url

    @activity_icon_url.setter
    def activity_icon_url(self, value):
        self._activity_icon_url = value
    @property
    def activity_jump_link(self):
        return self._activity_jump_link

    @activity_jump_link.setter
    def activity_jump_link(self, value):
        self._activity_jump_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGameopenpromoGamecenteractivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_icon_url' in response:
            self.activity_icon_url = response['activity_icon_url']
        if 'activity_jump_link' in response:
            self.activity_jump_link = response['activity_jump_link']
