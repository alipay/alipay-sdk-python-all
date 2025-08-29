#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpReportCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpReportCreateResponse, self).__init__()
        self._order_no = None
        self._out_biz_no = None
        self._page_redirection = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def page_redirection(self):
        return self._page_redirection

    @page_redirection.setter
    def page_redirection(self, value):
        self._page_redirection = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpReportCreateResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'page_redirection' in response:
            self.page_redirection = response['page_redirection']
