#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateComponentListResponse import TemplateComponentListResponse


class AlipayFincoreComplianceTemplateComponentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateComponentBatchqueryResponse, self).__init__()
        self._template_component_list_response_list = None

    @property
    def template_component_list_response_list(self):
        return self._template_component_list_response_list

    @template_component_list_response_list.setter
    def template_component_list_response_list(self, value):
        if isinstance(value, list):
            self._template_component_list_response_list = list()
            for i in value:
                if isinstance(i, TemplateComponentListResponse):
                    self._template_component_list_response_list.append(i)
                else:
                    self._template_component_list_response_list.append(TemplateComponentListResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateComponentBatchqueryResponse, self).parse_response_content(response_content)
        if 'template_component_list_response_list' in response:
            self.template_component_list_response_list = response['template_component_list_response_list']
