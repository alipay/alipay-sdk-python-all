#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoSignApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoSignApplyResponse, self).__init__()
        self._orderStr = None
        self._pageRedirectionData = None

    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value
    @property
    def pageRedirectionData(self):
        return self._pageRedirectionData

    @pageRedirectionData.setter
    def pageRedirectionData(self, value):
        self._pageRedirectionData = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoSignApplyResponse, self).parse_response_content(response_content)
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
        if 'pageRedirectionData' in response:
            self.pageRedirectionData = response['pageRedirectionData']
