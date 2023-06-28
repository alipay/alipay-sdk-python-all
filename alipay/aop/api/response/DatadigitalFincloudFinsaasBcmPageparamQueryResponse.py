#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasBcmPageparamQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasBcmPageparamQueryResponse, self).__init__()
        self._page_param_json = None

    @property
    def page_param_json(self):
        return self._page_param_json

    @page_param_json.setter
    def page_param_json(self, value):
        self._page_param_json = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasBcmPageparamQueryResponse, self).parse_response_content(response_content)
        if 'page_param_json' in response:
            self.page_param_json = response['page_param_json']
