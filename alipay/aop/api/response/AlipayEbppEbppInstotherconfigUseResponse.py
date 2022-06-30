#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OtherConfigVo import OtherConfigVo


class AlipayEbppEbppInstotherconfigUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEbppInstotherconfigUseResponse, self).__init__()
        self._current_page = None
        self._other_configs = None
        self._page_size = None
        self._total_count = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def other_configs(self):
        return self._other_configs

    @other_configs.setter
    def other_configs(self, value):
        if isinstance(value, list):
            self._other_configs = list()
            for i in value:
                if isinstance(i, OtherConfigVo):
                    self._other_configs.append(i)
                else:
                    self._other_configs.append(OtherConfigVo.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppEbppInstotherconfigUseResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'other_configs' in response:
            self.other_configs = response['other_configs']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
