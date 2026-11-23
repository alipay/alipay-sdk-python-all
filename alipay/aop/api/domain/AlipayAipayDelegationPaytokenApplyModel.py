#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayTokenConversationHistory import PayTokenConversationHistory
from alipay.aop.api.domain.OrderParams import OrderParams


class AlipayAipayDelegationPaytokenApplyModel(object):

    def __init__(self):
        self._agent_id = None
        self._conversation_history = None
        self._delegation_id = None
        self._order_params = None

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
        if isinstance(value, PayTokenConversationHistory):
            self._conversation_history = value
        else:
            self._conversation_history = PayTokenConversationHistory.from_alipay_dict(value)
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def order_params(self):
        return self._order_params

    @order_params.setter
    def order_params(self, value):
        if isinstance(value, OrderParams):
            self._order_params = value
        else:
            self._order_params = OrderParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.conversation_history:
            if hasattr(self.conversation_history, 'to_alipay_dict'):
                params['conversation_history'] = self.conversation_history.to_alipay_dict()
            else:
                params['conversation_history'] = self.conversation_history
        if self.delegation_id:
            if hasattr(self.delegation_id, 'to_alipay_dict'):
                params['delegation_id'] = self.delegation_id.to_alipay_dict()
            else:
                params['delegation_id'] = self.delegation_id
        if self.order_params:
            if hasattr(self.order_params, 'to_alipay_dict'):
                params['order_params'] = self.order_params.to_alipay_dict()
            else:
                params['order_params'] = self.order_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayDelegationPaytokenApplyModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'conversation_history' in d:
            o.conversation_history = d['conversation_history']
        if 'delegation_id' in d:
            o.delegation_id = d['delegation_id']
        if 'order_params' in d:
            o.order_params = d['order_params']
        return o


