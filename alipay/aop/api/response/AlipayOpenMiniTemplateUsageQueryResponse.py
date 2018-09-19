#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateUsageInfo import TemplateUsageInfo


class AlipayOpenMiniTemplateUsageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTemplateUsageQueryResponse, self).__init__()
        self._app_ids = None
        self._template_usage_info_list = None

    @property
    def app_ids(self):
        return self._app_ids

    @app_ids.setter
    def app_ids(self, value):
        if isinstance(value, list):
            self._app_ids = list()
            for i in value:
                self._app_ids.append(i)
    @property
    def template_usage_info_list(self):
        return self._template_usage_info_list

    @template_usage_info_list.setter
    def template_usage_info_list(self, value):
        if isinstance(value, list):
            self._template_usage_info_list = list()
            for i in value:
                if isinstance(i, TemplateUsageInfo):
                    self._template_usage_info_list.append(i)
                else:
                    self._template_usage_info_list.append(TemplateUsageInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTemplateUsageQueryResponse, self).parse_response_content(response_content)
        if 'app_ids' in response:
            self.app_ids = response['app_ids']
        if 'template_usage_info_list' in response:
            self.template_usage_info_list = response['template_usage_info_list']
