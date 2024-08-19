#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AnswerClarifyCardDetail import AnswerClarifyCardDetail
from alipay.aop.api.domain.AnswerItemDetail import AnswerItemDetail
from alipay.aop.api.domain.AnswerKnowledgeDetail import AnswerKnowledgeDetail
from alipay.aop.api.domain.AnswerServiceDetail import AnswerServiceDetail
from alipay.aop.api.domain.AnswerStreamDetail import AnswerStreamDetail
from alipay.aop.api.domain.AnswerTextDetail import AnswerTextDetail


class BotAnswer(object):

    def __init__(self):
        self._clarify_card = None
        self._item = None
        self._knowledge = None
        self._service = None
        self._stream = None
        self._text = None

    @property
    def clarify_card(self):
        return self._clarify_card

    @clarify_card.setter
    def clarify_card(self, value):
        if isinstance(value, list):
            self._clarify_card = list()
            for i in value:
                if isinstance(i, AnswerClarifyCardDetail):
                    self._clarify_card.append(i)
                else:
                    self._clarify_card.append(AnswerClarifyCardDetail.from_alipay_dict(i))
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, list):
            self._item = list()
            for i in value:
                if isinstance(i, AnswerItemDetail):
                    self._item.append(i)
                else:
                    self._item.append(AnswerItemDetail.from_alipay_dict(i))
    @property
    def knowledge(self):
        return self._knowledge

    @knowledge.setter
    def knowledge(self, value):
        if isinstance(value, list):
            self._knowledge = list()
            for i in value:
                if isinstance(i, AnswerKnowledgeDetail):
                    self._knowledge.append(i)
                else:
                    self._knowledge.append(AnswerKnowledgeDetail.from_alipay_dict(i))
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        if isinstance(value, list):
            self._service = list()
            for i in value:
                if isinstance(i, AnswerServiceDetail):
                    self._service.append(i)
                else:
                    self._service.append(AnswerServiceDetail.from_alipay_dict(i))
    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, value):
        if isinstance(value, AnswerStreamDetail):
            self._stream = value
        else:
            self._stream = AnswerStreamDetail.from_alipay_dict(value)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, list):
            self._text = list()
            for i in value:
                if isinstance(i, AnswerTextDetail):
                    self._text.append(i)
                else:
                    self._text.append(AnswerTextDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.clarify_card:
            if isinstance(self.clarify_card, list):
                for i in range(0, len(self.clarify_card)):
                    element = self.clarify_card[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clarify_card[i] = element.to_alipay_dict()
            if hasattr(self.clarify_card, 'to_alipay_dict'):
                params['clarify_card'] = self.clarify_card.to_alipay_dict()
            else:
                params['clarify_card'] = self.clarify_card
        if self.item:
            if isinstance(self.item, list):
                for i in range(0, len(self.item)):
                    element = self.item[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item[i] = element.to_alipay_dict()
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.knowledge:
            if isinstance(self.knowledge, list):
                for i in range(0, len(self.knowledge)):
                    element = self.knowledge[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.knowledge[i] = element.to_alipay_dict()
            if hasattr(self.knowledge, 'to_alipay_dict'):
                params['knowledge'] = self.knowledge.to_alipay_dict()
            else:
                params['knowledge'] = self.knowledge
        if self.service:
            if isinstance(self.service, list):
                for i in range(0, len(self.service)):
                    element = self.service[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service[i] = element.to_alipay_dict()
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.stream:
            if hasattr(self.stream, 'to_alipay_dict'):
                params['stream'] = self.stream.to_alipay_dict()
            else:
                params['stream'] = self.stream
        if self.text:
            if isinstance(self.text, list):
                for i in range(0, len(self.text)):
                    element = self.text[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text[i] = element.to_alipay_dict()
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BotAnswer()
        if 'clarify_card' in d:
            o.clarify_card = d['clarify_card']
        if 'item' in d:
            o.item = d['item']
        if 'knowledge' in d:
            o.knowledge = d['knowledge']
        if 'service' in d:
            o.service = d['service']
        if 'stream' in d:
            o.stream = d['stream']
        if 'text' in d:
            o.text = d['text']
        return o


