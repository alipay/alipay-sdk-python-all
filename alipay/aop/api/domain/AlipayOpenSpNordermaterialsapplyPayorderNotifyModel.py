#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsapplyPayorderNotifyModel(object):

    def __init__(self):
        self._shop_task_id = None

    @property
    def shop_task_id(self):
        return self._shop_task_id

    @shop_task_id.setter
    def shop_task_id(self, value):
        self._shop_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_task_id:
            if hasattr(self.shop_task_id, 'to_alipay_dict'):
                params['shop_task_id'] = self.shop_task_id.to_alipay_dict()
            else:
                params['shop_task_id'] = self.shop_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyPayorderNotifyModel()
        if 'shop_task_id' in d:
            o.shop_task_id = d['shop_task_id']
        return o


