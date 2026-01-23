#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpassporterBenefitCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterBenefitCreateResponse, self).__init__()
        self._open_id_list = None
        self._uid_list = None

    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
    @property
    def uid_list(self):
        return self._uid_list

    @uid_list.setter
    def uid_list(self, value):
        if isinstance(value, list):
            self._uid_list = list()
            for i in value:
                self._uid_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterBenefitCreateResponse, self).parse_response_content(response_content)
        if 'open_id_list' in response:
            self.open_id_list = response['open_id_list']
        if 'uid_list' in response:
            self.uid_list = response['uid_list']
