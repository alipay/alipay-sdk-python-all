#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasDesignPageApplyResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasDesignPageApplyResponse, self).__init__()
        self._page_code = None
        self._page_id = None

    @property
    def page_code(self):
        return self._page_code

    @page_code.setter
    def page_code(self, value):
        self._page_code = value
    @property
    def page_id(self):
        return self._page_id

    @page_id.setter
    def page_id(self, value):
        self._page_id = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasDesignPageApplyResponse, self).parse_response_content(response_content)
        if 'page_code' in response:
            self.page_code = response['page_code']
        if 'page_id' in response:
            self.page_id = response['page_id']
