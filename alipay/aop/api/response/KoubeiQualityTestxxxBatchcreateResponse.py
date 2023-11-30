#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiQualityTestxxxBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiQualityTestxxxBatchcreateResponse, self).__init__()
        self._oss_path = None
        self._www = None

    @property
    def oss_path(self):
        return self._oss_path

    @oss_path.setter
    def oss_path(self, value):
        self._oss_path = value
    @property
    def www(self):
        return self._www

    @www.setter
    def www(self, value):
        self._www = value

    def parse_response_content(self, response_content):
        response = super(KoubeiQualityTestxxxBatchcreateResponse, self).parse_response_content(response_content)
        if 'oss_path' in response:
            self.oss_path = response['oss_path']
        if 'www' in response:
            self.www = response['www']
