#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NbDrawSize import NbDrawSize
from alipay.aop.api.domain.NbInput import NbInput


class AlipayCloudNextbuilderAgentConfigGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudNextbuilderAgentConfigGetResponse, self).__init__()
        self._config_version = None
        self._create_questions = None
        self._draw_size = None
        self._inputs = None
        self._prequestions = None
        self._prologue = None
        self._published_time = None

    @property
    def config_version(self):
        return self._config_version

    @config_version.setter
    def config_version(self, value):
        self._config_version = value
    @property
    def create_questions(self):
        return self._create_questions

    @create_questions.setter
    def create_questions(self, value):
        self._create_questions = value
    @property
    def draw_size(self):
        return self._draw_size

    @draw_size.setter
    def draw_size(self, value):
        if isinstance(value, NbDrawSize):
            self._draw_size = value
        else:
            self._draw_size = NbDrawSize.from_alipay_dict(value)
    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        if isinstance(value, list):
            self._inputs = list()
            for i in value:
                if isinstance(i, NbInput):
                    self._inputs.append(i)
                else:
                    self._inputs.append(NbInput.from_alipay_dict(i))
    @property
    def prequestions(self):
        return self._prequestions

    @prequestions.setter
    def prequestions(self, value):
        if isinstance(value, list):
            self._prequestions = list()
            for i in value:
                self._prequestions.append(i)
    @property
    def prologue(self):
        return self._prologue

    @prologue.setter
    def prologue(self, value):
        self._prologue = value
    @property
    def published_time(self):
        return self._published_time

    @published_time.setter
    def published_time(self, value):
        self._published_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudNextbuilderAgentConfigGetResponse, self).parse_response_content(response_content)
        if 'config_version' in response:
            self.config_version = response['config_version']
        if 'create_questions' in response:
            self.create_questions = response['create_questions']
        if 'draw_size' in response:
            self.draw_size = response['draw_size']
        if 'inputs' in response:
            self.inputs = response['inputs']
        if 'prequestions' in response:
            self.prequestions = response['prequestions']
        if 'prologue' in response:
            self.prologue = response['prologue']
        if 'published_time' in response:
            self.published_time = response['published_time']
