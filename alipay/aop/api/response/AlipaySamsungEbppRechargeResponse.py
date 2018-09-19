#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySamsungEbppRechargeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySamsungEbppRechargeResponse, self).__init__()
        self._page_retrun = None

    @property
    def page_retrun(self):
        return self._page_retrun

    @page_retrun.setter
    def page_retrun(self, value):
        self._page_retrun = value

    def parse_response_content(self, response_content):
        response = super(AlipaySamsungEbppRechargeResponse, self).parse_response_content(response_content)
        if 'page_retrun' in response:
            self.page_retrun = response['page_retrun']
