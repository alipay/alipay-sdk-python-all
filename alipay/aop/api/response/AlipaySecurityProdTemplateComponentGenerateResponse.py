#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateElementLinkDTO import TemplateElementLinkDTO


class AlipaySecurityProdTemplateComponentGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateComponentGenerateResponse, self).__init__()
        self._template_element_link_dto = None

    @property
    def template_element_link_dto(self):
        return self._template_element_link_dto

    @template_element_link_dto.setter
    def template_element_link_dto(self, value):
        if isinstance(value, TemplateElementLinkDTO):
            self._template_element_link_dto = value
        else:
            self._template_element_link_dto = TemplateElementLinkDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateComponentGenerateResponse, self).parse_response_content(response_content)
        if 'template_element_link_dto' in response:
            self.template_element_link_dto = response['template_element_link_dto']
