#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HttpsDomainCert import HttpsDomainCert


class AlipayCloudCloudbaseHttpscerthostingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpscerthostingQueryResponse, self).__init__()
        self._domains = None

    @property
    def domains(self):
        return self._domains

    @domains.setter
    def domains(self, value):
        if isinstance(value, list):
            self._domains = list()
            for i in value:
                if isinstance(i, HttpsDomainCert):
                    self._domains.append(i)
                else:
                    self._domains.append(HttpsDomainCert.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpscerthostingQueryResponse, self).parse_response_content(response_content)
        if 'domains' in response:
            self.domains = response['domains']
