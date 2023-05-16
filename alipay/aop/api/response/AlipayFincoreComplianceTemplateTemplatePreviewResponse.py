#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplatePreviewResponse import TemplatePreviewResponse


class AlipayFincoreComplianceTemplateTemplatePreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateTemplatePreviewResponse, self).__init__()
        self._template_preview_response = None

    @property
    def template_preview_response(self):
        return self._template_preview_response

    @template_preview_response.setter
    def template_preview_response(self, value):
        if isinstance(value, list):
            self._template_preview_response = list()
            for i in value:
                if isinstance(i, TemplatePreviewResponse):
                    self._template_preview_response.append(i)
                else:
                    self._template_preview_response.append(TemplatePreviewResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateTemplatePreviewResponse, self).parse_response_content(response_content)
        if 'template_preview_response' in response:
            self.template_preview_response = response['template_preview_response']
