#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFileConvertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFileConvertQueryResponse, self).__init__()
        self._pdf_presigned_url = None
        self._task_result = None

    @property
    def pdf_presigned_url(self):
        return self._pdf_presigned_url

    @pdf_presigned_url.setter
    def pdf_presigned_url(self, value):
        self._pdf_presigned_url = value
    @property
    def task_result(self):
        return self._task_result

    @task_result.setter
    def task_result(self, value):
        self._task_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFileConvertQueryResponse, self).parse_response_content(response_content)
        if 'pdf_presigned_url' in response:
            self.pdf_presigned_url = response['pdf_presigned_url']
        if 'task_result' in response:
            self.task_result = response['task_result']
