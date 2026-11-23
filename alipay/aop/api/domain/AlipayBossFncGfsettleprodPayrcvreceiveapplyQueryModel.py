#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayrcvReceiveApplyOrder import PayrcvReceiveApplyOrder


class AlipayBossFncGfsettleprodPayrcvreceiveapplyQueryModel(object):

    def __init__(self):
        self._payrcv_receive_apply_order = None

    @property
    def payrcv_receive_apply_order(self):
        return self._payrcv_receive_apply_order

    @payrcv_receive_apply_order.setter
    def payrcv_receive_apply_order(self, value):
        if isinstance(value, PayrcvReceiveApplyOrder):
            self._payrcv_receive_apply_order = value
        else:
            self._payrcv_receive_apply_order = PayrcvReceiveApplyOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.payrcv_receive_apply_order:
            if hasattr(self.payrcv_receive_apply_order, 'to_alipay_dict'):
                params['payrcv_receive_apply_order'] = self.payrcv_receive_apply_order.to_alipay_dict()
            else:
                params['payrcv_receive_apply_order'] = self.payrcv_receive_apply_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodPayrcvreceiveapplyQueryModel()
        if 'payrcv_receive_apply_order' in d:
            o.payrcv_receive_apply_order = d['payrcv_receive_apply_order']
        return o


