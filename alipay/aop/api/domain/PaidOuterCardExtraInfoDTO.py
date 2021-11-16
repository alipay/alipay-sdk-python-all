#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaidOuterCardCycleInfoDTO import PaidOuterCardCycleInfoDTO
from alipay.aop.api.domain.PaidOuterCardPurchaseInfoDTO import PaidOuterCardPurchaseInfoDTO


class PaidOuterCardExtraInfoDTO(object):

    def __init__(self):
        self._action = None
        self._cycle_info = None
        self._purchase_info = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def cycle_info(self):
        return self._cycle_info

    @cycle_info.setter
    def cycle_info(self, value):
        if isinstance(value, PaidOuterCardCycleInfoDTO):
            self._cycle_info = value
        else:
            self._cycle_info = PaidOuterCardCycleInfoDTO.from_alipay_dict(value)
    @property
    def purchase_info(self):
        return self._purchase_info

    @purchase_info.setter
    def purchase_info(self, value):
        if isinstance(value, PaidOuterCardPurchaseInfoDTO):
            self._purchase_info = value
        else:
            self._purchase_info = PaidOuterCardPurchaseInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.cycle_info:
            if hasattr(self.cycle_info, 'to_alipay_dict'):
                params['cycle_info'] = self.cycle_info.to_alipay_dict()
            else:
                params['cycle_info'] = self.cycle_info
        if self.purchase_info:
            if hasattr(self.purchase_info, 'to_alipay_dict'):
                params['purchase_info'] = self.purchase_info.to_alipay_dict()
            else:
                params['purchase_info'] = self.purchase_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardExtraInfoDTO()
        if 'action' in d:
            o.action = d['action']
        if 'cycle_info' in d:
            o.cycle_info = d['cycle_info']
        if 'purchase_info' in d:
            o.purchase_info = d['purchase_info']
        return o


