#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FengdieTemplate import FengdieTemplate


class AlipayMarketingToolFengdieTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolFengdieTemplateQueryResponse, self).__init__()
        self._template = None

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, list):
            self._template = list()
            for i in value:
                if isinstance(i, FengdieTemplate):
                    self._template.append(i)
                else:
                    self._template.append(FengdieTemplate.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolFengdieTemplateQueryResponse, self).parse_response_content(response_content)
        if 'template' in response:
            self.template = response['template']
