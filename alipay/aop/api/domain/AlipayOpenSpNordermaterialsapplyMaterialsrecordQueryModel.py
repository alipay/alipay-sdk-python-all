#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsapplyMaterialsrecordQueryModel(object):

    def __init__(self):
        self._record_id = None
        self._shop_biz_id = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def shop_biz_id(self):
        return self._shop_biz_id

    @shop_biz_id.setter
    def shop_biz_id(self, value):
        self._shop_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.shop_biz_id:
            if hasattr(self.shop_biz_id, 'to_alipay_dict'):
                params['shop_biz_id'] = self.shop_biz_id.to_alipay_dict()
            else:
                params['shop_biz_id'] = self.shop_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyMaterialsrecordQueryModel()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'shop_biz_id' in d:
            o.shop_biz_id = d['shop_biz_id']
        return o


