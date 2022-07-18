#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppxVersionConfigVo import AppxVersionConfigVo


class AlipayOpenMiniInnerVersionproportionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerVersionproportionQueryResponse, self).__init__()
        self._appx_version_config_vos = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerVersionproportionQueryResponse, self).parse_response_content(response_content)
        if 'appx_version_config_vos' in response:
            self.appx_version_config_vos = response['appx_version_config_vos']
