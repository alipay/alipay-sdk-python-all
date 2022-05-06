#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppTestInfo import AppTestInfo


class AlipayOpenOperationIspTestUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationIspTestUseResponse, self).__init__()
        self._app_info = None
        self._output = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        if isinstance(value, list):
            self._app_info = list()
            for i in value:
                if isinstance(i, AppTestInfo):
                    self._app_info.append(i)
                else:
                    self._app_info.append(AppTestInfo.from_alipay_dict(i))
    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationIspTestUseResponse, self).parse_response_content(response_content)
        if 'app_info' in response:
            self.app_info = response['app_info']
        if 'output' in response:
            self.output = response['output']
