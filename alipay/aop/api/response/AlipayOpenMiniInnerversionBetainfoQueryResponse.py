#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PluginBetaItemInfo import PluginBetaItemInfo


class AlipayOpenMiniInnerversionBetainfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionBetainfoQueryResponse, self).__init__()
        self._plugin_beta_item_list = None
        self._status = None

    @property
    def plugin_beta_item_list(self):
        return self._plugin_beta_item_list

    @plugin_beta_item_list.setter
    def plugin_beta_item_list(self, value):
        if isinstance(value, list):
            self._plugin_beta_item_list = list()
            for i in value:
                if isinstance(i, PluginBetaItemInfo):
                    self._plugin_beta_item_list.append(i)
                else:
                    self._plugin_beta_item_list.append(PluginBetaItemInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionBetainfoQueryResponse, self).parse_response_content(response_content)
        if 'plugin_beta_item_list' in response:
            self.plugin_beta_item_list = response['plugin_beta_item_list']
        if 'status' in response:
            self.status = response['status']
