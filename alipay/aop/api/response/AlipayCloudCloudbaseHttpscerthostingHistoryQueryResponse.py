#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HttpsDomainCertHistory import HttpsDomainCertHistory


class AlipayCloudCloudbaseHttpscerthostingHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpscerthostingHistoryQueryResponse, self).__init__()
        self._historys = None

    @property
    def historys(self):
        return self._historys

    @historys.setter
    def historys(self, value):
        if isinstance(value, list):
            self._historys = list()
            for i in value:
                if isinstance(i, HttpsDomainCertHistory):
                    self._historys.append(i)
                else:
                    self._historys.append(HttpsDomainCertHistory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpscerthostingHistoryQueryResponse, self).parse_response_content(response_content)
        if 'historys' in response:
            self.historys = response['historys']
