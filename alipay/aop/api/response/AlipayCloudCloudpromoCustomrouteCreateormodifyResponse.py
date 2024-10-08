#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RouteInfo import RouteInfo


class AlipayCloudCloudpromoCustomrouteCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoCustomrouteCreateormodifyResponse, self).__init__()
        self._item_id = None
        self._routes = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def routes(self):
        return self._routes

    @routes.setter
    def routes(self, value):
        if isinstance(value, list):
            self._routes = list()
            for i in value:
                if isinstance(i, RouteInfo):
                    self._routes.append(i)
                else:
                    self._routes.append(RouteInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoCustomrouteCreateormodifyResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'routes' in response:
            self.routes = response['routes']
