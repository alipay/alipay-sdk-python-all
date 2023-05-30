#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniTemplateApp import MiniTemplateApp


class AlipayOpenMiniTemplatelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTemplatelistQueryResponse, self).__init__()
        self._app_list = None

    @property
    def app_list(self):
        return self._app_list

    @app_list.setter
    def app_list(self, value):
        if isinstance(value, list):
            self._app_list = list()
            for i in value:
                if isinstance(i, MiniTemplateApp):
                    self._app_list.append(i)
                else:
                    self._app_list.append(MiniTemplateApp.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTemplatelistQueryResponse, self).parse_response_content(response_content)
        if 'app_list' in response:
            self.app_list = response['app_list']
