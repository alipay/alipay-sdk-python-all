#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AvailableResourceModel import AvailableResourceModel


class AlipayIserviceIcontrolFreeresourcesbycodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIcontrolFreeresourcesbycodeQueryResponse, self).__init__()
        self._resources = None

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, AvailableResourceModel):
                    self._resources.append(i)
                else:
                    self._resources.append(AvailableResourceModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIcontrolFreeresourcesbycodeQueryResponse, self).parse_response_content(response_content)
        if 'resources' in response:
            self.resources = response['resources']
