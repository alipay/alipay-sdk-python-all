#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentBaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentBaseinfoQueryResponse, self).__init__()
        self._app_desc = None
        self._app_label = None
        self._app_logo = None
        self._app_name = None
        self._app_tone = None
        self._background = None
        self._card_bottom = None
        self._card_guide = None
        self._card_type = None
        self._continue_ask = None
        self._custom_card_body = None
        self._custom_card_id = None
        self._support_qa_mode = None

    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_label(self):
        return self._app_label

    @app_label.setter
    def app_label(self, value):
        if isinstance(value, list):
            self._app_label = list()
            for i in value:
                self._app_label.append(i)
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_tone(self):
        return self._app_tone

    @app_tone.setter
    def app_tone(self, value):
        self._app_tone = value
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value
    @property
    def card_bottom(self):
        return self._card_bottom

    @card_bottom.setter
    def card_bottom(self, value):
        self._card_bottom = value
    @property
    def card_guide(self):
        return self._card_guide

    @card_guide.setter
    def card_guide(self, value):
        self._card_guide = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def continue_ask(self):
        return self._continue_ask

    @continue_ask.setter
    def continue_ask(self, value):
        self._continue_ask = value
    @property
    def custom_card_body(self):
        return self._custom_card_body

    @custom_card_body.setter
    def custom_card_body(self, value):
        self._custom_card_body = value
    @property
    def custom_card_id(self):
        return self._custom_card_id

    @custom_card_id.setter
    def custom_card_id(self, value):
        self._custom_card_id = value
    @property
    def support_qa_mode(self):
        return self._support_qa_mode

    @support_qa_mode.setter
    def support_qa_mode(self, value):
        if isinstance(value, list):
            self._support_qa_mode = list()
            for i in value:
                self._support_qa_mode.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentBaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'app_desc' in response:
            self.app_desc = response['app_desc']
        if 'app_label' in response:
            self.app_label = response['app_label']
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_tone' in response:
            self.app_tone = response['app_tone']
        if 'background' in response:
            self.background = response['background']
        if 'card_bottom' in response:
            self.card_bottom = response['card_bottom']
        if 'card_guide' in response:
            self.card_guide = response['card_guide']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'continue_ask' in response:
            self.continue_ask = response['continue_ask']
        if 'custom_card_body' in response:
            self.custom_card_body = response['custom_card_body']
        if 'custom_card_id' in response:
            self.custom_card_id = response['custom_card_id']
        if 'support_qa_mode' in response:
            self.support_qa_mode = response['support_qa_mode']
