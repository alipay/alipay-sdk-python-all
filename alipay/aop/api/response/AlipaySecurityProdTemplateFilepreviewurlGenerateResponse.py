#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GetOfficePreviewURLResponse import GetOfficePreviewURLResponse


class AlipaySecurityProdTemplateFilepreviewurlGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateFilepreviewurlGenerateResponse, self).__init__()
        self._get_office_preview_url_response = None

    @property
    def get_office_preview_url_response(self):
        return self._get_office_preview_url_response

    @get_office_preview_url_response.setter
    def get_office_preview_url_response(self, value):
        if isinstance(value, GetOfficePreviewURLResponse):
            self._get_office_preview_url_response = value
        else:
            self._get_office_preview_url_response = GetOfficePreviewURLResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateFilepreviewurlGenerateResponse, self).parse_response_content(response_content)
        if 'get_office_preview_url_response' in response:
            self.get_office_preview_url_response = response['get_office_preview_url_response']
