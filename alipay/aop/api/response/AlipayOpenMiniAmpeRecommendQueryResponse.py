#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeRecommendQueryResponse, self).__init__()
        self._card_url = None
        self._show_widget = None

    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value
    @property
    def show_widget(self):
        return self._show_widget

    @show_widget.setter
    def show_widget(self, value):
        self._show_widget = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeRecommendQueryResponse, self).parse_response_content(response_content)
        if 'card_url' in response:
            self.card_url = response['card_url']
        if 'show_widget' in response:
            self.show_widget = response['show_widget']
