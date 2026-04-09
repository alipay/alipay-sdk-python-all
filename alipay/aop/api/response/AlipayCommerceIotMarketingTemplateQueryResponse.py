#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ISPTemplateInfo import ISPTemplateInfo


class AlipayCommerceIotMarketingTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMarketingTemplateQueryResponse, self).__init__()
        self._template_info_list = None

    @property
    def template_info_list(self):
        return self._template_info_list

    @template_info_list.setter
    def template_info_list(self, value):
        if isinstance(value, list):
            self._template_info_list = list()
            for i in value:
                if isinstance(i, ISPTemplateInfo):
                    self._template_info_list.append(i)
                else:
                    self._template_info_list.append(ISPTemplateInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMarketingTemplateQueryResponse, self).parse_response_content(response_content)
        if 'template_info_list' in response:
            self.template_info_list = response['template_info_list']
