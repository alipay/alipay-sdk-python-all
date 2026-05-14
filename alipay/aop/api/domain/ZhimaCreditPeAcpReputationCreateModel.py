#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeAcpReputationCreateModel(object):

    def __init__(self):
        self._agent_id = None
        self._event_type = None
        self._goods_name = None
        self._relate_agent_id = None
        self._trade_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def relate_agent_id(self):
        return self._relate_agent_id

    @relate_agent_id.setter
    def relate_agent_id(self, value):
        self._relate_agent_id = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.relate_agent_id:
            if hasattr(self.relate_agent_id, 'to_alipay_dict'):
                params['relate_agent_id'] = self.relate_agent_id.to_alipay_dict()
            else:
                params['relate_agent_id'] = self.relate_agent_id
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeAcpReputationCreateModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'relate_agent_id' in d:
            o.relate_agent_id = d['relate_agent_id']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


