#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderUserinfoExpoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderUserinfoExpoCreateResponse, self).__init__()
        self._vid_list = None

    @property
    def vid_list(self):
        return self._vid_list

    @vid_list.setter
    def vid_list(self, value):
        if isinstance(value, list):
            self._vid_list = list()
            for i in value:
                self._vid_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderUserinfoExpoCreateResponse, self).parse_response_content(response_content)
        if 'vid_list' in response:
            self.vid_list = response['vid_list']
