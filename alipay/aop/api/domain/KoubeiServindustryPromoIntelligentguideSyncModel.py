#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IntelligentGuideTradeInfo import IntelligentGuideTradeInfo


class KoubeiServindustryPromoIntelligentguideSyncModel(object):

    def __init__(self):
        self._partner_id = None
        self._trade_infos = None

    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def trade_infos(self):
        return self._trade_infos

    @trade_infos.setter
    def trade_infos(self, value):
        if isinstance(value, list):
            self._trade_infos = list()
            for i in value:
                if isinstance(i, IntelligentGuideTradeInfo):
                    self._trade_infos.append(i)
                else:
                    self._trade_infos.append(IntelligentGuideTradeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.trade_infos:
            if isinstance(self.trade_infos, list):
                for i in range(0, len(self.trade_infos)):
                    element = self.trade_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_infos[i] = element.to_alipay_dict()
            if hasattr(self.trade_infos, 'to_alipay_dict'):
                params['trade_infos'] = self.trade_infos.to_alipay_dict()
            else:
                params['trade_infos'] = self.trade_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryPromoIntelligentguideSyncModel()
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'trade_infos' in d:
            o.trade_infos = d['trade_infos']
        return o


