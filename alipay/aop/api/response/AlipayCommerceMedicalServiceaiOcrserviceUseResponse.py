#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServiceaiOcrserviceUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceaiOcrserviceUseResponse, self).__init__()
        self._afts_id = None
        self._file_ext = None
        self._ocr_result = None
        self._out_pic_url = None
        self._pic_url = None
        self._task_category = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def file_ext(self):
        return self._file_ext

    @file_ext.setter
    def file_ext(self, value):
        self._file_ext = value
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
    def task_category(self):
        return self._task_category

    @task_category.setter
    def task_category(self, value):
        self._task_category = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceaiOcrserviceUseResponse, self).parse_response_content(response_content)
        if 'afts_id' in response:
            self.afts_id = response['afts_id']
        if 'file_ext' in response:
            self.file_ext = response['file_ext']
        if 'ocr_result' in response:
            self.ocr_result = response['ocr_result']
        if 'out_pic_url' in response:
            self.out_pic_url = response['out_pic_url']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
        if 'task_category' in response:
            self.task_category = response['task_category']
