#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsserviceprodSerprogressSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsserviceprodSerprogressSyncResponse, self).__init__()
        self._progress_no = None

    @property
    def progress_no(self):
        return self._progress_no

    @progress_no.setter
    def progress_no(self, value):
        self._progress_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsserviceprodSerprogressSyncResponse, self).parse_response_content(response_content)
        if 'progress_no' in response:
            self.progress_no = response['progress_no']
