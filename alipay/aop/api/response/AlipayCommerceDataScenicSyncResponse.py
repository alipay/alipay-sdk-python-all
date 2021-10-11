#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDataScenicSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataScenicSyncResponse, self).__init__()
        self._desc = None
        self._outer_id = None
        self._scenic_app_id = None
        self._scenic_id = None
        self._status = None
        self._zfb_scenic_id = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def zfb_scenic_id(self):
        return self._zfb_scenic_id

    @zfb_scenic_id.setter
    def zfb_scenic_id(self, value):
        self._zfb_scenic_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataScenicSyncResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'outer_id' in response:
            self.outer_id = response['outer_id']
        if 'scenic_app_id' in response:
            self.scenic_app_id = response['scenic_app_id']
        if 'scenic_id' in response:
            self.scenic_id = response['scenic_id']
        if 'status' in response:
            self.status = response['status']
        if 'zfb_scenic_id' in response:
            self.zfb_scenic_id = response['zfb_scenic_id']
