#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFatigueContent import DeliveryFatigueContent
from alipay.aop.api.domain.StrategyGroupFatigue import StrategyGroupFatigue


class DeliveryFatigueInfo(object):

    def __init__(self):
        self._content_fatigue = None
        self._scm = None
        self._strategy_group_fatigue = None
        self._ucdp_fatigue_info = None

    @property
    def content_fatigue(self):
        return self._content_fatigue

    @content_fatigue.setter
    def content_fatigue(self, value):
        if isinstance(value, DeliveryFatigueContent):
            self._content_fatigue = value
        else:
            self._content_fatigue = DeliveryFatigueContent.from_alipay_dict(value)
    @property
    def scm(self):
        return self._scm

    @scm.setter
    def scm(self, value):
        self._scm = value
    @property
    def strategy_group_fatigue(self):
        return self._strategy_group_fatigue

    @strategy_group_fatigue.setter
    def strategy_group_fatigue(self, value):
        if isinstance(value, list):
            self._strategy_group_fatigue = list()
            for i in value:
                if isinstance(i, StrategyGroupFatigue):
                    self._strategy_group_fatigue.append(i)
                else:
                    self._strategy_group_fatigue.append(StrategyGroupFatigue.from_alipay_dict(i))
    @property
    def ucdp_fatigue_info(self):
        return self._ucdp_fatigue_info

    @ucdp_fatigue_info.setter
    def ucdp_fatigue_info(self, value):
        self._ucdp_fatigue_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_fatigue:
            if hasattr(self.content_fatigue, 'to_alipay_dict'):
                params['content_fatigue'] = self.content_fatigue.to_alipay_dict()
            else:
                params['content_fatigue'] = self.content_fatigue
        if self.scm:
            if hasattr(self.scm, 'to_alipay_dict'):
                params['scm'] = self.scm.to_alipay_dict()
            else:
                params['scm'] = self.scm
        if self.strategy_group_fatigue:
            if isinstance(self.strategy_group_fatigue, list):
                for i in range(0, len(self.strategy_group_fatigue)):
                    element = self.strategy_group_fatigue[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.strategy_group_fatigue[i] = element.to_alipay_dict()
            if hasattr(self.strategy_group_fatigue, 'to_alipay_dict'):
                params['strategy_group_fatigue'] = self.strategy_group_fatigue.to_alipay_dict()
            else:
                params['strategy_group_fatigue'] = self.strategy_group_fatigue
        if self.ucdp_fatigue_info:
            if hasattr(self.ucdp_fatigue_info, 'to_alipay_dict'):
                params['ucdp_fatigue_info'] = self.ucdp_fatigue_info.to_alipay_dict()
            else:
                params['ucdp_fatigue_info'] = self.ucdp_fatigue_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryFatigueInfo()
        if 'content_fatigue' in d:
            o.content_fatigue = d['content_fatigue']
        if 'scm' in d:
            o.scm = d['scm']
        if 'strategy_group_fatigue' in d:
            o.strategy_group_fatigue = d['strategy_group_fatigue']
        if 'ucdp_fatigue_info' in d:
            o.ucdp_fatigue_info = d['ucdp_fatigue_info']
        return o


