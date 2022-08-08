#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PageInfoDTO import PageInfoDTO


class DatadigitalFincloudFinsaasDesignPageGetResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasDesignPageGetResponse, self).__init__()
        self._page_code = None
        self._page_info = None

    @property
    def page_code(self):
        return self._page_code

    @page_code.setter
    def page_code(self, value):
        self._page_code = value
    @property
    def page_info(self):
        return self._page_info

    @page_info.setter
    def page_info(self, value):
        if isinstance(value, PageInfoDTO):
            self._page_info = value
        else:
            self._page_info = PageInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasDesignPageGetResponse, self).parse_response_content(response_content)
        if 'page_code' in response:
            self.page_code = response['page_code']
        if 'page_info' in response:
            self.page_info = response['page_info']
