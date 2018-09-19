#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimAttachmentConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimAttachmentConfirmResponse, self).__init__()
        self._lost_files = None
        self._status = None

    @property
    def lost_files(self):
        return self._lost_files

    @lost_files.setter
    def lost_files(self, value):
        if isinstance(value, list):
            self._lost_files = list()
            for i in value:
                self._lost_files.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimAttachmentConfirmResponse, self).parse_response_content(response_content)
        if 'lost_files' in response:
            self.lost_files = response['lost_files']
        if 'status' in response:
            self.status = response['status']
