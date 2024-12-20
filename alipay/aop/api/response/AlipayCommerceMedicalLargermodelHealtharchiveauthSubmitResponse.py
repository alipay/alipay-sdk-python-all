#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalLargermodelHealtharchiveauthSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelHealtharchiveauthSubmitResponse, self).__init__()
        self._auth_code = None
        self._org_id = None
        self._scene_code = None
        self._status = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelHealtharchiveauthSubmitResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'org_id' in response:
            self.org_id = response['org_id']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'status' in response:
            self.status = response['status']
