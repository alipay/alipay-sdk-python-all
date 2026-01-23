#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServiceaiOcrserviceUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceaiOcrserviceUploadResponse, self).__init__()
        self._afts_id = None
        self._file_type = None
        self._kv_result = None
        self._ocr_result = None
        self._out_pic_url = None
        self._pic_url = None
        self._task_type = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def kv_result(self):
        return self._kv_result

    @kv_result.setter
    def kv_result(self, value):
        self._kv_result = value
    @property
    def ocr_result(self):
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, value):
        self._ocr_result = value
    @property
    def out_pic_url(self):
        return self._out_pic_url

    @out_pic_url.setter
    def out_pic_url(self, value):
        self._out_pic_url = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceaiOcrserviceUploadResponse, self).parse_response_content(response_content)
        if 'afts_id' in response:
            self.afts_id = response['afts_id']
        if 'file_type' in response:
            self.file_type = response['file_type']
        if 'kv_result' in response:
            self.kv_result = response['kv_result']
        if 'ocr_result' in response:
            self.ocr_result = response['ocr_result']
        if 'out_pic_url' in response:
            self.out_pic_url = response['out_pic_url']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
        if 'task_type' in response:
            self.task_type = response['task_type']
