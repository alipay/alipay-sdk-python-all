#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ComponentContextResponse import ComponentContextResponse


class AlipayIserviceComponentcontextQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceComponentcontextQueryResponse, self).__init__()
        self._component_context_response = None

    @property
    def component_context_response(self):
        return self._component_context_response

    @component_context_response.setter
    def component_context_response(self, value):
        if isinstance(value, list):
            self._component_context_response = list()
            for i in value:
                if isinstance(i, ComponentContextResponse):
                    self._component_context_response.append(i)
                else:
                    self._component_context_response.append(ComponentContextResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceComponentcontextQueryResponse, self).parse_response_content(response_content)
        if 'component_context_response' in response:
            self.component_context_response = response['component_context_response']
