#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankMarketingBkcustgrowprodCardstyleCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankMarketingBkcustgrowprodCardstyleCreateResponse, self).__init__()
        self._selected = None
        self._style_id = None
        self._success = None
        self._template_id = None

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value
    @property
    def style_id(self):
        return self._style_id

    @style_id.setter
    def style_id(self, value):
        self._style_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(MybankMarketingBkcustgrowprodCardstyleCreateResponse, self).parse_response_content(response_content)
        if 'selected' in response:
            self.selected = response['selected']
        if 'style_id' in response:
            self.style_id = response['style_id']
        if 'success' in response:
            self.success = response['success']
        if 'template_id' in response:
            self.template_id = response['template_id']
