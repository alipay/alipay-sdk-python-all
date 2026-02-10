#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AxfItemAttrTemplate import AxfItemAttrTemplate


class AlipayCommerceLifeserviceCategorytemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceCategorytemplateQueryResponse, self).__init__()
        self._attr_template = None

    @property
    def attr_template(self):
        return self._attr_template

    @attr_template.setter
    def attr_template(self, value):
        if isinstance(value, list):
            self._attr_template = list()
            for i in value:
                if isinstance(i, AxfItemAttrTemplate):
                    self._attr_template.append(i)
                else:
                    self._attr_template.append(AxfItemAttrTemplate.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceCategorytemplateQueryResponse, self).parse_response_content(response_content)
        if 'attr_template' in response:
            self.attr_template = response['attr_template']
