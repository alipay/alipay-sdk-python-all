#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseFunctionGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionGetResponse, self).__init__()
        self._description = None
        self._function_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._image_name = None
        self._quota_name = None
        self._status = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def quota_name(self):
        return self._quota_name

    @quota_name.setter
    def quota_name(self, value):
        self._quota_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionGetResponse, self).parse_response_content(response_content)
        if 'description' in response:
            self.description = response['description']
        if 'function_name' in response:
            self.function_name = response['function_name']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'image_name' in response:
            self.image_name = response['image_name']
        if 'quota_name' in response:
            self.quota_name = response['quota_name']
        if 'status' in response:
            self.status = response['status']
