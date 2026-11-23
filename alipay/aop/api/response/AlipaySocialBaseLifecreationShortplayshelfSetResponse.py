#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseLifecreationShortplayshelfSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationShortplayshelfSetResponse, self).__init__()
        self._album_id = None
        self._reason = None
        self._status = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationShortplayshelfSetResponse, self).parse_response_content(response_content)
        if 'album_id' in response:
            self.album_id = response['album_id']
        if 'reason' in response:
            self.reason = response['reason']
        if 'status' in response:
            self.status = response['status']
