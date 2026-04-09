#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Conversation import Conversation


class AlipayUserAgreementDelegationSignModel(object):

    def __init__(self):
        self._ai_pay_agreement_no = None
        self._conversation_history = None
        self._delegation_desc = None
        self._delegation_scene = None
        self._delegation_tag = None
        self._external_delegation_id = None
        self._no_pwd_agreement_no = None

    @property
    def ai_pay_agreement_no(self):
        return self._ai_pay_agreement_no

    @ai_pay_agreement_no.setter
    def ai_pay_agreement_no(self, value):
        self._ai_pay_agreement_no = value
    @property
    def conversation_history(self):
        return self._conversation_history

    @conversation_history.setter
    def conversation_history(self, value):
        if isinstance(value, list):
            self._conversation_history = list()
            for i in value:
                if isinstance(i, Conversation):
                    self._conversation_history.append(i)
                else:
                    self._conversation_history.append(Conversation.from_alipay_dict(i))
    @property
    def delegation_desc(self):
        return self._delegation_desc

    @delegation_desc.setter
    def delegation_desc(self, value):
        self._delegation_desc = value
    @property
    def delegation_scene(self):
        return self._delegation_scene

    @delegation_scene.setter
    def delegation_scene(self, value):
        self._delegation_scene = value
    @property
    def delegation_tag(self):
        return self._delegation_tag

    @delegation_tag.setter
    def delegation_tag(self, value):
        self._delegation_tag = value
    @property
    def external_delegation_id(self):
        return self._external_delegation_id

    @external_delegation_id.setter
    def external_delegation_id(self, value):
        self._external_delegation_id = value
    @property
    def no_pwd_agreement_no(self):
        return self._no_pwd_agreement_no

    @no_pwd_agreement_no.setter
    def no_pwd_agreement_no(self, value):
        self._no_pwd_agreement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_pay_agreement_no:
            if hasattr(self.ai_pay_agreement_no, 'to_alipay_dict'):
                params['ai_pay_agreement_no'] = self.ai_pay_agreement_no.to_alipay_dict()
            else:
                params['ai_pay_agreement_no'] = self.ai_pay_agreement_no
        if self.conversation_history:
            if isinstance(self.conversation_history, list):
                for i in range(0, len(self.conversation_history)):
                    element = self.conversation_history[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversation_history[i] = element.to_alipay_dict()
            if hasattr(self.conversation_history, 'to_alipay_dict'):
                params['conversation_history'] = self.conversation_history.to_alipay_dict()
            else:
                params['conversation_history'] = self.conversation_history
        if self.delegation_desc:
            if hasattr(self.delegation_desc, 'to_alipay_dict'):
                params['delegation_desc'] = self.delegation_desc.to_alipay_dict()
            else:
                params['delegation_desc'] = self.delegation_desc
        if self.delegation_scene:
            if hasattr(self.delegation_scene, 'to_alipay_dict'):
                params['delegation_scene'] = self.delegation_scene.to_alipay_dict()
            else:
                params['delegation_scene'] = self.delegation_scene
        if self.delegation_tag:
            if hasattr(self.delegation_tag, 'to_alipay_dict'):
                params['delegation_tag'] = self.delegation_tag.to_alipay_dict()
            else:
                params['delegation_tag'] = self.delegation_tag
        if self.external_delegation_id:
            if hasattr(self.external_delegation_id, 'to_alipay_dict'):
                params['external_delegation_id'] = self.external_delegation_id.to_alipay_dict()
            else:
                params['external_delegation_id'] = self.external_delegation_id
        if self.no_pwd_agreement_no:
            if hasattr(self.no_pwd_agreement_no, 'to_alipay_dict'):
                params['no_pwd_agreement_no'] = self.no_pwd_agreement_no.to_alipay_dict()
            else:
                params['no_pwd_agreement_no'] = self.no_pwd_agreement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementDelegationSignModel()
        if 'ai_pay_agreement_no' in d:
            o.ai_pay_agreement_no = d['ai_pay_agreement_no']
        if 'conversation_history' in d:
            o.conversation_history = d['conversation_history']
        if 'delegation_desc' in d:
            o.delegation_desc = d['delegation_desc']
        if 'delegation_scene' in d:
            o.delegation_scene = d['delegation_scene']
        if 'delegation_tag' in d:
            o.delegation_tag = d['delegation_tag']
        if 'external_delegation_id' in d:
            o.external_delegation_id = d['external_delegation_id']
        if 'no_pwd_agreement_no' in d:
            o.no_pwd_agreement_no = d['no_pwd_agreement_no']
        return o


