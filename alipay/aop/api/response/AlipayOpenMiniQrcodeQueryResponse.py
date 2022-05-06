#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QrCodeRouteGroup import QrCodeRouteGroup


class AlipayOpenMiniQrcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniQrcodeQueryResponse, self).__init__()
        self._qr_code_route_groups = None
        self._total_items = None

    @property
    def qr_code_route_groups(self):
        return self._qr_code_route_groups

    @qr_code_route_groups.setter
    def qr_code_route_groups(self, value):
        if isinstance(value, list):
            self._qr_code_route_groups = list()
            for i in value:
                if isinstance(i, QrCodeRouteGroup):
                    self._qr_code_route_groups.append(i)
                else:
                    self._qr_code_route_groups.append(QrCodeRouteGroup.from_alipay_dict(i))
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniQrcodeQueryResponse, self).parse_response_content(response_content)
        if 'qr_code_route_groups' in response:
            self.qr_code_route_groups = response['qr_code_route_groups']
        if 'total_items' in response:
            self.total_items = response['total_items']
