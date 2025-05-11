#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveLivedataCurrentliveQueryModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._alipay_public_id = None
        self._need_unit = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def need_unit(self):
        return self._need_unit

    @need_unit.setter
    def need_unit(self, value):
        self._need_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.need_unit:
            if hasattr(self.need_unit, 'to_alipay_dict'):
                params['need_unit'] = self.need_unit.to_alipay_dict()
            else:
                params['need_unit'] = self.need_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveLivedataCurrentliveQueryModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'need_unit' in d:
            o.need_unit = d['need_unit']
        return o


