#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentWelcomeCardDTO(object):

    def __init__(self):
        self._agent_name = None
        self._card_icon = None
        self._card_slogan = None
        self._intro_desc = None
        self._intro_title = None
        self._pre_question = None

    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def card_icon(self):
        return self._card_icon

    @card_icon.setter
    def card_icon(self, value):
        self._card_icon = value
    @property
    def card_slogan(self):
        return self._card_slogan

    @card_slogan.setter
    def card_slogan(self, value):
        self._card_slogan = value
    @property
    def intro_desc(self):
        return self._intro_desc

    @intro_desc.setter
    def intro_desc(self, value):
        self._intro_desc = value
    @property
    def intro_title(self):
        return self._intro_title

    @intro_title.setter
    def intro_title(self, value):
        self._intro_title = value
    @property
    def pre_question(self):
        return self._pre_question

    @pre_question.setter
    def pre_question(self, value):
        if isinstance(value, list):
            self._pre_question = list()
            for i in value:
                self._pre_question.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.card_icon:
            if hasattr(self.card_icon, 'to_alipay_dict'):
                params['card_icon'] = self.card_icon.to_alipay_dict()
            else:
                params['card_icon'] = self.card_icon
        if self.card_slogan:
            if hasattr(self.card_slogan, 'to_alipay_dict'):
                params['card_slogan'] = self.card_slogan.to_alipay_dict()
            else:
                params['card_slogan'] = self.card_slogan
        if self.intro_desc:
            if hasattr(self.intro_desc, 'to_alipay_dict'):
                params['intro_desc'] = self.intro_desc.to_alipay_dict()
            else:
                params['intro_desc'] = self.intro_desc
        if self.intro_title:
            if hasattr(self.intro_title, 'to_alipay_dict'):
                params['intro_title'] = self.intro_title.to_alipay_dict()
            else:
                params['intro_title'] = self.intro_title
        if self.pre_question:
            if isinstance(self.pre_question, list):
                for i in range(0, len(self.pre_question)):
                    element = self.pre_question[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pre_question[i] = element.to_alipay_dict()
            if hasattr(self.pre_question, 'to_alipay_dict'):
                params['pre_question'] = self.pre_question.to_alipay_dict()
            else:
                params['pre_question'] = self.pre_question
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentWelcomeCardDTO()
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'card_icon' in d:
            o.card_icon = d['card_icon']
        if 'card_slogan' in d:
            o.card_slogan = d['card_slogan']
        if 'intro_desc' in d:
            o.intro_desc = d['intro_desc']
        if 'intro_title' in d:
            o.intro_title = d['intro_title']
        if 'pre_question' in d:
            o.pre_question = d['pre_question']
        return o


