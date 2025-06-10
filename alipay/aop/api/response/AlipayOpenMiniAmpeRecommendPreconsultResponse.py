#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeRecommendPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeRecommendPreconsultResponse, self).__init__()
        self._show_widget = None

    @property
    def show_widget(self):
        return self._show_widget

    @show_widget.setter
    def show_widget(self, value):
        self._show_widget = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeRecommendPreconsultResponse, self).parse_response_content(response_content)
        if 'show_widget' in response:
            self.show_widget = response['show_widget']
