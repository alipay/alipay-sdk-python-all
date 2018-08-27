#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantSingleDataUploadResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantSingleDataUploadResponse, self).__init__()
        self._biz_ext_params = None
        self._task_id = None

    @property
    def biz_ext_params(self):
        return self._biz_ext_params

    @biz_ext_params.setter
    def biz_ext_params(self, value):
        self._biz_ext_params = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantSingleDataUploadResponse, self).parse_response_content(response_content)
        if 'biz_ext_params' in response:
            self.biz_ext_params = response['biz_ext_params']
        if 'task_id' in response:
            self.task_id = response['task_id']
