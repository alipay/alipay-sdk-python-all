#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessParams import AccessParams
from alipay.aop.api.domain.Conversation import Conversation
from alipay.aop.api.domain.DelegationParams import DelegationParams


class AlipayUserAgreementDelegationApplyModel(object):

    def __init__(self):
        self._access_params = None
        self._agent_id = None
        self._conversation_history = None
        self._delegation_params = None
        self._external_agreement_no = None
        self._personal_product_code = None

    @property
    def access_params(self):
        return self._access_params

    @access_params.setter
    def access_params(self, value):
        if isinstance(value, AccessParams):
            self._access_params = value
        else:
            self._access_params = AccessParams.from_alipay_dict(value)
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
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
    def delegation_params(self):
        return self._delegation_params

    @delegation_params.setter
    def delegation_params(self, value):
        if isinstance(value, DelegationParams):
            self._delegation_params = value
        else:
            self._delegation_params = DelegationParams.from_alipay_dict(value)
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_params:
            if hasattr(self.access_params, 'to_alipay_dict'):
                params['access_params'] = self.access_params.to_alipay_dict()
            else:
                params['access_params'] = self.access_params
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
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
        if self.delegation_params:
            if hasattr(self.delegation_params, 'to_alipay_dict'):
                params['delegation_params'] = self.delegation_params.to_alipay_dict()
            else:
                params['delegation_params'] = self.delegation_params
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementDelegationApplyModel()
        if 'access_params' in d:
            o.access_params = d['access_params']
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'conversation_history' in d:
            o.conversation_history = d['conversation_history']
        if 'delegation_params' in d:
            o.delegation_params = d['delegation_params']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        return o


