#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NotifyInfo import NotifyInfo


class AlipayOpenAppNotifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppNotifyQueryResponse, self).__init__()
        self._notify_info_list = None

    @property
    def notify_info_list(self):
        return self._notify_info_list

    @notify_info_list.setter
    def notify_info_list(self, value):
        if isinstance(value, list):
            self._notify_info_list = list()
            for i in value:
                if isinstance(i, NotifyInfo):
                    self._notify_info_list.append(i)
                else:
                    self._notify_info_list.append(NotifyInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppNotifyQueryResponse, self).parse_response_content(response_content)
        if 'notify_info_list' in response:
            self.notify_info_list = response['notify_info_list']
