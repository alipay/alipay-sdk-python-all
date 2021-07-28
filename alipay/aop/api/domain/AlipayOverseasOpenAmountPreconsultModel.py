#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionISVAgentInfoDTO import TuitionISVAgentInfoDTO
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class AlipayOverseasOpenAmountPreconsultModel(object):

    def __init__(self):
        self._agent_info = None
        self._original_amount = None
        self._reference_id = None

    @property
    def agent_info(self):
        return self._agent_info

    @agent_info.setter
    def agent_info(self, value):
        if isinstance(value, TuitionISVAgentInfoDTO):
            self._agent_info = value
        else:
            self._agent_info = TuitionISVAgentInfoDTO.from_alipay_dict(value)
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._original_amount = value
        else:
            self._original_amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_info:
            if hasattr(self.agent_info, 'to_alipay_dict'):
                params['agent_info'] = self.agent_info.to_alipay_dict()
            else:
                params['agent_info'] = self.agent_info
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.reference_id:
            if hasattr(self.reference_id, 'to_alipay_dict'):
                params['reference_id'] = self.reference_id.to_alipay_dict()
            else:
                params['reference_id'] = self.reference_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenAmountPreconsultModel()
        if 'agent_info' in d:
            o.agent_info = d['agent_info']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        return o


