#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateVersionDTO import TemplateVersionDTO


class AlipaySecurityProdTemplateVersionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateVersionQueryResponse, self).__init__()
        self._template_version_dto = None

    @property
    def template_version_dto(self):
        return self._template_version_dto

    @template_version_dto.setter
    def template_version_dto(self, value):
        if isinstance(value, TemplateVersionDTO):
            self._template_version_dto = value
        else:
            self._template_version_dto = TemplateVersionDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateVersionQueryResponse, self).parse_response_content(response_content)
        if 'template_version_dto' in response:
            self.template_version_dto = response['template_version_dto']
