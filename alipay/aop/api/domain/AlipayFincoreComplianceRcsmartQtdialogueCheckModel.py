#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DialogueParam import DialogueParam
from alipay.aop.api.domain.Dialogue import Dialogue


class AlipayFincoreComplianceRcsmartQtdialogueCheckModel(object):

    def __init__(self):
        self._app_name = None
        self._app_token = None
        self._biz_code = None
        self._dialogue_param = None
        self._dialogues = None
        self._scene_code = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def dialogue_param(self):
        return self._dialogue_param

    @dialogue_param.setter
    def dialogue_param(self, value):
        if isinstance(value, DialogueParam):
            self._dialogue_param = value
        else:
            self._dialogue_param = DialogueParam.from_alipay_dict(value)
    @property
    def dialogues(self):
        return self._dialogues

    @dialogues.setter
    def dialogues(self, value):
        if isinstance(value, list):
            self._dialogues = list()
            for i in value:
                if isinstance(i, Dialogue):
                    self._dialogues.append(i)
                else:
                    self._dialogues.append(Dialogue.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.dialogue_param:
            if hasattr(self.dialogue_param, 'to_alipay_dict'):
                params['dialogue_param'] = self.dialogue_param.to_alipay_dict()
            else:
                params['dialogue_param'] = self.dialogue_param
        if self.dialogues:
            if isinstance(self.dialogues, list):
                for i in range(0, len(self.dialogues)):
                    element = self.dialogues[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dialogues[i] = element.to_alipay_dict()
            if hasattr(self.dialogues, 'to_alipay_dict'):
                params['dialogues'] = self.dialogues.to_alipay_dict()
            else:
                params['dialogues'] = self.dialogues
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcsmartQtdialogueCheckModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'dialogue_param' in d:
            o.dialogue_param = d['dialogue_param']
        if 'dialogues' in d:
            o.dialogues = d['dialogues']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


