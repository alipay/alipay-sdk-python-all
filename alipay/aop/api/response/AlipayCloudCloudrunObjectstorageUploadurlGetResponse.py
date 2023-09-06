#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OssPostUploadFormData import OssPostUploadFormData


class AlipayCloudCloudrunObjectstorageUploadurlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageUploadurlGetResponse, self).__init__()
        self._file_id = None
        self._form_data = None
        self._upload_url = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def form_data(self):
        return self._form_data

    @form_data.setter
    def form_data(self, value):
        if isinstance(value, list):
            self._form_data = list()
            for i in value:
                if isinstance(i, OssPostUploadFormData):
                    self._form_data.append(i)
                else:
                    self._form_data.append(OssPostUploadFormData.from_alipay_dict(i))
    @property
    def upload_url(self):
        return self._upload_url

    @upload_url.setter
    def upload_url(self, value):
        self._upload_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageUploadurlGetResponse, self).parse_response_content(response_content)
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'form_data' in response:
            self.form_data = response['form_data']
        if 'upload_url' in response:
            self.upload_url = response['upload_url']
