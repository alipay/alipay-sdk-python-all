#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AttributeVO import AttributeVO


class AlipayOpenAppDeliveryTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppDeliveryTemplateQueryResponse, self).__init__()
        self._attrs = None
        self._delivery_type = None
        self._template_id = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, AttributeVO):
            self._attrs = value
        else:
            self._attrs = AttributeVO.from_alipay_dict(value)
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppDeliveryTemplateQueryResponse, self).parse_response_content(response_content)
        if 'attrs' in response:
            self.attrs = response['attrs']
        if 'delivery_type' in response:
            self.delivery_type = response['delivery_type']
        if 'template_id' in response:
            self.template_id = response['template_id']
