#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalLlmAnswerDTO import MedicalLlmAnswerDTO


class LlmServiceDTO(object):

    def __init__(self):
        self._answer = None
        self._answer_type = None
        self._ant_session_id = None
        self._chat_id = None
        self._intention = None
        self._is_finished = None
        self._is_with_draw = None
        self._scene_code = None
        self._template_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, list):
            self._answer = list()
            for i in value:
                if isinstance(i, MedicalLlmAnswerDTO):
                    self._answer.append(i)
                else:
                    self._answer.append(MedicalLlmAnswerDTO.from_alipay_dict(i))
    @property
    def answer_type(self):
        return self._answer_type

    @answer_type.setter
    def answer_type(self, value):
        self._answer_type = value
    @property
    def ant_session_id(self):
        return self._ant_session_id

    @ant_session_id.setter
    def ant_session_id(self, value):
        self._ant_session_id = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def intention(self):
        return self._intention

    @intention.setter
    def intention(self, value):
        self._intention = value
    @property
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, value):
        self._is_finished = value
    @property
    def is_with_draw(self):
        return self._is_with_draw

    @is_with_draw.setter
    def is_with_draw(self, value):
        self._is_with_draw = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer:
            if isinstance(self.answer, list):
                for i in range(0, len(self.answer)):
                    element = self.answer[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.answer[i] = element.to_alipay_dict()
            if hasattr(self.answer, 'to_alipay_dict'):
                params['answer'] = self.answer.to_alipay_dict()
            else:
                params['answer'] = self.answer
        if self.answer_type:
            if hasattr(self.answer_type, 'to_alipay_dict'):
                params['answer_type'] = self.answer_type.to_alipay_dict()
            else:
                params['answer_type'] = self.answer_type
        if self.ant_session_id:
            if hasattr(self.ant_session_id, 'to_alipay_dict'):
                params['ant_session_id'] = self.ant_session_id.to_alipay_dict()
            else:
                params['ant_session_id'] = self.ant_session_id
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.intention:
            if hasattr(self.intention, 'to_alipay_dict'):
                params['intention'] = self.intention.to_alipay_dict()
            else:
                params['intention'] = self.intention
        if self.is_finished:
            if hasattr(self.is_finished, 'to_alipay_dict'):
                params['is_finished'] = self.is_finished.to_alipay_dict()
            else:
                params['is_finished'] = self.is_finished
        if self.is_with_draw:
            if hasattr(self.is_with_draw, 'to_alipay_dict'):
                params['is_with_draw'] = self.is_with_draw.to_alipay_dict()
            else:
                params['is_with_draw'] = self.is_with_draw
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LlmServiceDTO()
        if 'answer' in d:
            o.answer = d['answer']
        if 'answer_type' in d:
            o.answer_type = d['answer_type']
        if 'ant_session_id' in d:
            o.ant_session_id = d['ant_session_id']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'intention' in d:
            o.intention = d['intention']
        if 'is_finished' in d:
            o.is_finished = d['is_finished']
        if 'is_with_draw' in d:
            o.is_with_draw = d['is_with_draw']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


