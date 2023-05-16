#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateNewModelDTO import TemplateNewModelDTO


class AlipayFincoreComplianceTemplateTemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateTemplateBatchqueryResponse, self).__init__()
        self._template_new_models = None

    @property
    def template_new_models(self):
        return self._template_new_models

    @template_new_models.setter
    def template_new_models(self, value):
        if isinstance(value, list):
            self._template_new_models = list()
            for i in value:
                if isinstance(i, TemplateNewModelDTO):
                    self._template_new_models.append(i)
                else:
                    self._template_new_models.append(TemplateNewModelDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateTemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'template_new_models' in response:
            self.template_new_models = response['template_new_models']
