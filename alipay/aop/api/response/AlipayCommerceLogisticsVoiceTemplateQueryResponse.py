#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsVoiceTemplate import LogisticsVoiceTemplate


class AlipayCommerceLogisticsVoiceTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsVoiceTemplateQueryResponse, self).__init__()
        self._template_list = None
        self._total = None

    @property
    def template_list(self):
        return self._template_list

    @template_list.setter
    def template_list(self, value):
        if isinstance(value, list):
            self._template_list = list()
            for i in value:
                if isinstance(i, LogisticsVoiceTemplate):
                    self._template_list.append(i)
                else:
                    self._template_list.append(LogisticsVoiceTemplate.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsVoiceTemplateQueryResponse, self).parse_response_content(response_content)
        if 'template_list' in response:
            self.template_list = response['template_list']
        if 'total' in response:
            self.total = response['total']
