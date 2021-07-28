#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionISVAgentInfoDTO import TuitionISVAgentInfoDTO


class AlipayOverseasOpenPreorderCancelModel(object):

    def __init__(self):
        self._agent_info = None
        self._pre_order_id = None

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
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_info:
            if hasattr(self.agent_info, 'to_alipay_dict'):
                params['agent_info'] = self.agent_info.to_alipay_dict()
            else:
                params['agent_info'] = self.agent_info
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenPreorderCancelModel()
        if 'agent_info' in d:
            o.agent_info = d['agent_info']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


