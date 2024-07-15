#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PositionDeliveryFatigueInfo import PositionDeliveryFatigueInfo


class AntfortuneStockDeliverydetailFatigueSyncModel(object):

    def __init__(self):
        self._action = None
        self._agreement_no = None
        self._position_delivery_model = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def position_delivery_model(self):
        return self._position_delivery_model

    @position_delivery_model.setter
    def position_delivery_model(self, value):
        if isinstance(value, list):
            self._position_delivery_model = list()
            for i in value:
                if isinstance(i, PositionDeliveryFatigueInfo):
                    self._position_delivery_model.append(i)
                else:
                    self._position_delivery_model.append(PositionDeliveryFatigueInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.position_delivery_model:
            if isinstance(self.position_delivery_model, list):
                for i in range(0, len(self.position_delivery_model)):
                    element = self.position_delivery_model[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.position_delivery_model[i] = element.to_alipay_dict()
            if hasattr(self.position_delivery_model, 'to_alipay_dict'):
                params['position_delivery_model'] = self.position_delivery_model.to_alipay_dict()
            else:
                params['position_delivery_model'] = self.position_delivery_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockDeliverydetailFatigueSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'position_delivery_model' in d:
            o.position_delivery_model = d['position_delivery_model']
        return o


