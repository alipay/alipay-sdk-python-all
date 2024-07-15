#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateDTO import TemplateDTO


class AlipaySecurityProdTemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateBatchqueryResponse, self).__init__()
        self._template_dto_list = None

    @property
    def template_dto_list(self):
        return self._template_dto_list

    @template_dto_list.setter
    def template_dto_list(self, value):
        if isinstance(value, list):
            self._template_dto_list = list()
            for i in value:
                if isinstance(i, TemplateDTO):
                    self._template_dto_list.append(i)
                else:
                    self._template_dto_list.append(TemplateDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'template_dto_list' in response:
            self.template_dto_list = response['template_dto_list']
