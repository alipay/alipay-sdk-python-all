#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertDomainProvider import CertDomainProvider


class AlipayCloudCloudbaseHttpscerthostingDomainproviderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpscerthostingDomainproviderQueryResponse, self).__init__()
        self._providers = None

    @property
    def providers(self):
        return self._providers

    @providers.setter
    def providers(self, value):
        if isinstance(value, list):
            self._providers = list()
            for i in value:
                if isinstance(i, CertDomainProvider):
                    self._providers.append(i)
                else:
                    self._providers.append(CertDomainProvider.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpscerthostingDomainproviderQueryResponse, self).parse_response_content(response_content)
        if 'providers' in response:
            self.providers = response['providers']
