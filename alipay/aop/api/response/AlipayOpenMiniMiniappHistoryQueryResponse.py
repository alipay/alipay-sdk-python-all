#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppHistoryInfo import MiniAppHistoryInfo


class AlipayOpenMiniMiniappHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappHistoryQueryResponse, self).__init__()
        self._mini_app_history_infos = None

    @property
    def mini_app_history_infos(self):
        return self._mini_app_history_infos

    @mini_app_history_infos.setter
    def mini_app_history_infos(self, value):
        if isinstance(value, list):
            self._mini_app_history_infos = list()
            for i in value:
                if isinstance(i, MiniAppHistoryInfo):
                    self._mini_app_history_infos.append(i)
                else:
                    self._mini_app_history_infos.append(MiniAppHistoryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappHistoryQueryResponse, self).parse_response_content(response_content)
        if 'mini_app_history_infos' in response:
            self.mini_app_history_infos = response['mini_app_history_infos']
