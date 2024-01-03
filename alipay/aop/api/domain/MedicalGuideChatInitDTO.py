#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalGuideContentDTO import MedicalGuideContentDTO
from alipay.aop.api.domain.MedicalGuideDialogDTO import MedicalGuideDialogDTO


class MedicalGuideChatInitDTO(object):

    def __init__(self):
        self._content = None
        self._dialog_history = None
        self._logo = None
        self._name = None
        self._session_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, MedicalGuideContentDTO):
            self._content = value
        else:
            self._content = MedicalGuideContentDTO.from_alipay_dict(value)
    @property
    def dialog_history(self):
        return self._dialog_history

    @dialog_history.setter
    def dialog_history(self, value):
        if isinstance(value, list):
            self._dialog_history = list()
            for i in value:
                if isinstance(i, MedicalGuideDialogDTO):
                    self._dialog_history.append(i)
                else:
                    self._dialog_history.append(MedicalGuideDialogDTO.from_alipay_dict(i))
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.dialog_history:
            if isinstance(self.dialog_history, list):
                for i in range(0, len(self.dialog_history)):
                    element = self.dialog_history[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dialog_history[i] = element.to_alipay_dict()
            if hasattr(self.dialog_history, 'to_alipay_dict'):
                params['dialog_history'] = self.dialog_history.to_alipay_dict()
            else:
                params['dialog_history'] = self.dialog_history
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalGuideChatInitDTO()
        if 'content' in d:
            o.content = d['content']
        if 'dialog_history' in d:
            o.dialog_history = d['dialog_history']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


