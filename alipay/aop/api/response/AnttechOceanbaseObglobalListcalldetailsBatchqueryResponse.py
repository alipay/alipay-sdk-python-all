#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CallDetailDTO import CallDetailDTO


class AnttechOceanbaseObglobalListcalldetailsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalListcalldetailsBatchqueryResponse, self).__init__()
        self._biz_error_code = None
        self._biz_error_msg = None
        self._biz_success = None
        self._current_page = None
        self._page_size = None
        self._result = None
        self._total_size = None

    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def biz_error_msg(self):
        return self._biz_error_msg

    @biz_error_msg.setter
    def biz_error_msg(self, value):
        self._biz_error_msg = value
    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, CallDetailDTO):
                    self._result.append(i)
                else:
                    self._result.append(CallDetailDTO.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalListcalldetailsBatchqueryResponse, self).parse_response_content(response_content)
        if 'biz_error_code' in response:
            self.biz_error_code = response['biz_error_code']
        if 'biz_error_msg' in response:
            self.biz_error_msg = response['biz_error_msg']
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'result' in response:
            self.result = response['result']
        if 'total_size' in response:
            self.total_size = response['total_size']
