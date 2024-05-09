#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntfarmOrnamentResource import AntfarmOrnamentResource


class AlipaySocialAntfarmOrnamentresourceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntfarmOrnamentresourceBatchqueryResponse, self).__init__()
        self._ornament_resource_list = None
        self._spine_resource_url = None

    @property
    def ornament_resource_list(self):
        return self._ornament_resource_list

    @ornament_resource_list.setter
    def ornament_resource_list(self, value):
        if isinstance(value, list):
            self._ornament_resource_list = list()
            for i in value:
                if isinstance(i, AntfarmOrnamentResource):
                    self._ornament_resource_list.append(i)
                else:
                    self._ornament_resource_list.append(AntfarmOrnamentResource.from_alipay_dict(i))
    @property
    def spine_resource_url(self):
        return self._spine_resource_url

    @spine_resource_url.setter
    def spine_resource_url(self, value):
        self._spine_resource_url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntfarmOrnamentresourceBatchqueryResponse, self).parse_response_content(response_content)
        if 'ornament_resource_list' in response:
            self.ornament_resource_list = response['ornament_resource_list']
        if 'spine_resource_url' in response:
            self.spine_resource_url = response['spine_resource_url']
