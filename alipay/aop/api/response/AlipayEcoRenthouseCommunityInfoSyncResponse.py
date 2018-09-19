#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRenthouseCommunityInfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRenthouseCommunityInfoSyncResponse, self).__init__()
        self._comm_req_id = None
        self._status = None

    @property
    def comm_req_id(self):
        return self._comm_req_id

    @comm_req_id.setter
    def comm_req_id(self, value):
        self._comm_req_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRenthouseCommunityInfoSyncResponse, self).parse_response_content(response_content)
        if 'comm_req_id' in response:
            self.comm_req_id = response['comm_req_id']
        if 'status' in response:
            self.status = response['status']
