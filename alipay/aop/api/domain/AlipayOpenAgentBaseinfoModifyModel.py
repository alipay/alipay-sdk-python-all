#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentBaseinfoModifyModel(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = self.app_desc.to_alipay_dict()
            else:
                params['app_desc'] = self.app_desc
        if self.app_label:
            if isinstance(self.app_label, list):
                for i in range(0, len(self.app_label)):
                    element = self.app_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_label[i] = element.to_alipay_dict()
            if hasattr(self.app_label, 'to_alipay_dict'):
                params['app_label'] = self.app_label.to_alipay_dict()
            else:
                params['app_label'] = self.app_label
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_tone:
            if hasattr(self.app_tone, 'to_alipay_dict'):
                params['app_tone'] = self.app_tone.to_alipay_dict()
            else:
                params['app_tone'] = self.app_tone
        if self.background:
            if hasattr(self.background, 'to_alipay_dict'):
                params['background'] = self.background.to_alipay_dict()
            else:
                params['background'] = self.background
        if self.card_bottom:
            if hasattr(self.card_bottom, 'to_alipay_dict'):
                params['card_bottom'] = self.card_bottom.to_alipay_dict()
            else:
                params['card_bottom'] = self.card_bottom
        if self.card_guide:
            if hasattr(self.card_guide, 'to_alipay_dict'):
                params['card_guide'] = self.card_guide.to_alipay_dict()
            else:
                params['card_guide'] = self.card_guide
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.continue_ask:
            if hasattr(self.continue_ask, 'to_alipay_dict'):
                params['continue_ask'] = self.continue_ask.to_alipay_dict()
            else:
                params['continue_ask'] = self.continue_ask
        if self.custom_card_body:
            if hasattr(self.custom_card_body, 'to_alipay_dict'):
                params['custom_card_body'] = self.custom_card_body.to_alipay_dict()
            else:
                params['custom_card_body'] = self.custom_card_body
        if self.custom_card_id:
            if hasattr(self.custom_card_id, 'to_alipay_dict'):
                params['custom_card_id'] = self.custom_card_id.to_alipay_dict()
            else:
                params['custom_card_id'] = self.custom_card_id
        if self.support_qa_mode:
            if isinstance(self.support_qa_mode, list):
                for i in range(0, len(self.support_qa_mode)):
                    element = self.support_qa_mode[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_qa_mode[i] = element.to_alipay_dict()
            if hasattr(self.support_qa_mode, 'to_alipay_dict'):
                params['support_qa_mode'] = self.support_qa_mode.to_alipay_dict()
            else:
                params['support_qa_mode'] = self.support_qa_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentBaseinfoModifyModel()
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_label' in d:
            o.app_label = d['app_label']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_tone' in d:
            o.app_tone = d['app_tone']
        if 'background' in d:
            o.background = d['background']
        if 'card_bottom' in d:
            o.card_bottom = d['card_bottom']
        if 'card_guide' in d:
            o.card_guide = d['card_guide']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'continue_ask' in d:
            o.continue_ask = d['continue_ask']
        if 'custom_card_body' in d:
            o.custom_card_body = d['custom_card_body']
        if 'custom_card_id' in d:
            o.custom_card_id = d['custom_card_id']
        if 'support_qa_mode' in d:
            o.support_qa_mode = d['support_qa_mode']
        return o


