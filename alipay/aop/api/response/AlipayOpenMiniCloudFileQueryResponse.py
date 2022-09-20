#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniCloudFileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudFileQueryResponse, self).__init__()
        self._absolute_path = None
        self._cloud_id = None
        self._creator = None
        self._download_url = None
        self._enable = None
        self._file_id = None
        self._file_name = None
        self._file_type = None
        self._path = None

    @property
    def absolute_path(self):
        return self._absolute_path

    @absolute_path.setter
    def absolute_path(self, value):
        self._absolute_path = value
    @property
    def cloud_id(self):
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, value):
        self._cloud_id = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudFileQueryResponse, self).parse_response_content(response_content)
        if 'absolute_path' in response:
            self.absolute_path = response['absolute_path']
        if 'cloud_id' in response:
            self.cloud_id = response['cloud_id']
        if 'creator' in response:
            self.creator = response['creator']
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'enable' in response:
            self.enable = response['enable']
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'file_type' in response:
            self.file_type = response['file_type']
        if 'path' in response:
            self.path = response['path']
