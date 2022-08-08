#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PageTemplateInfoDTO import PageTemplateInfoDTO


class DatadigitalFincloudFinsaasDesignPagetemplateGetResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasDesignPagetemplateGetResponse, self).__init__()
        self._template_code = None
        self._template_info = None

    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_info(self):
        return self._template_info

    @template_info.setter
    def template_info(self, value):
        if isinstance(value, PageTemplateInfoDTO):
            self._template_info = value
        else:
            self._template_info = PageTemplateInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasDesignPagetemplateGetResponse, self).parse_response_content(response_content)
        if 'template_code' in response:
            self.template_code = response['template_code']
        if 'template_info' in response:
            self.template_info = response['template_info']
