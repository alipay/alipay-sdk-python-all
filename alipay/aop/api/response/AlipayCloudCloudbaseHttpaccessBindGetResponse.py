#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseHttpaccessBindGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpaccessBindGetResponse, self).__init__()
        self._bind_id = None
        self._domain_name = None
        self._function_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._is_custom = None
        self._need_sign = None
        self._path = None

    @property
    def bind_id(self):
        return self._bind_id

    @bind_id.setter
    def bind_id(self, value):
        self._bind_id = value
    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        self._domain_name = value
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
    def is_custom(self):
        return self._is_custom

    @is_custom.setter
    def is_custom(self, value):
        self._is_custom = value
    @property
    def need_sign(self):
        return self._need_sign

    @need_sign.setter
    def need_sign(self, value):
        self._need_sign = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpaccessBindGetResponse, self).parse_response_content(response_content)
        if 'bind_id' in response:
            self.bind_id = response['bind_id']
        if 'domain_name' in response:
            self.domain_name = response['domain_name']
        if 'function_name' in response:
            self.function_name = response['function_name']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'is_custom' in response:
            self.is_custom = response['is_custom']
        if 'need_sign' in response:
            self.need_sign = response['need_sign']
        if 'path' in response:
            self.path = response['path']
