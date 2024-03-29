#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppxVersionConfigVo import AppxVersionConfigVo


class AlipayOpenMiniInnerVersionproportionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerVersionproportionQueryResponse, self).__init__()
        self._appx_version_config_vos = None
        self._page_num = None
        self._page_size = None
        self._total_number = None

    @property
    def appx_version_config_vos(self):
        return self._appx_version_config_vos

    @appx_version_config_vos.setter
    def appx_version_config_vos(self, value):
        if isinstance(value, list):
            self._appx_version_config_vos = list()
            for i in value:
                if isinstance(i, AppxVersionConfigVo):
                    self._appx_version_config_vos.append(i)
                else:
                    self._appx_version_config_vos.append(AppxVersionConfigVo.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerVersionproportionQueryResponse, self).parse_response_content(response_content)
        if 'appx_version_config_vos' in response:
            self.appx_version_config_vos = response['appx_version_config_vos']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_number' in response:
            self.total_number = response['total_number']
