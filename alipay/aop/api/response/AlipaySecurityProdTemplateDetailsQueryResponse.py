#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateDTO import TemplateDTO


class AlipaySecurityProdTemplateDetailsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateDetailsQueryResponse, self).__init__()
        self._template_dto = None

    @property
    def template_dto(self):
        return self._template_dto

    @template_dto.setter
    def template_dto(self, value):
        if isinstance(value, TemplateDTO):
            self._template_dto = value
        else:
            self._template_dto = TemplateDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateDetailsQueryResponse, self).parse_response_content(response_content)
        if 'template_dto' in response:
            self.template_dto = response['template_dto']
