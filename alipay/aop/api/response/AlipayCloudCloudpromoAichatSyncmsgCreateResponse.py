#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChatReference import ChatReference


class AlipayCloudCloudpromoAichatSyncmsgCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAichatSyncmsgCreateResponse, self).__init__()
        self._answer = None
        self._biz_trans_data = None
        self._question = None
        self._references = None
        self._related_questions = None
        self._request_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
    @property
    def biz_trans_data(self):
        return self._biz_trans_data

    @biz_trans_data.setter
    def biz_trans_data(self, value):
        self._biz_trans_data = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, value):
        if isinstance(value, list):
            self._references = list()
            for i in value:
                if isinstance(i, ChatReference):
                    self._references.append(i)
                else:
                    self._references.append(ChatReference.from_alipay_dict(i))
    @property
    def related_questions(self):
        return self._related_questions

    @related_questions.setter
    def related_questions(self, value):
        if isinstance(value, list):
            self._related_questions = list()
            for i in value:
                self._related_questions.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAichatSyncmsgCreateResponse, self).parse_response_content(response_content)
        if 'answer' in response:
            self.answer = response['answer']
        if 'biz_trans_data' in response:
            self.biz_trans_data = response['biz_trans_data']
        if 'question' in response:
            self.question = response['question']
        if 'references' in response:
            self.references = response['references']
        if 'related_questions' in response:
            self.related_questions = response['related_questions']
        if 'request_id' in response:
            self.request_id = response['request_id']
