#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GrasslandCertDetail import GrasslandCertDetail


class AlipaySocialAntforestGrasslandcertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestGrasslandcertQueryResponse, self).__init__()
        self._grassland_cert_detail_list = None
        self._has_more = None
        self._next_cursor = None

    @property
    def grassland_cert_detail_list(self):
        return self._grassland_cert_detail_list

    @grassland_cert_detail_list.setter
    def grassland_cert_detail_list(self, value):
        if isinstance(value, list):
            self._grassland_cert_detail_list = list()
            for i in value:
                if isinstance(i, GrasslandCertDetail):
                    self._grassland_cert_detail_list.append(i)
                else:
                    self._grassland_cert_detail_list.append(GrasslandCertDetail.from_alipay_dict(i))
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def next_cursor(self):
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self._next_cursor = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestGrasslandcertQueryResponse, self).parse_response_content(response_content)
        if 'grassland_cert_detail_list' in response:
            self.grassland_cert_detail_list = response['grassland_cert_detail_list']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'next_cursor' in response:
            self.next_cursor = response['next_cursor']
