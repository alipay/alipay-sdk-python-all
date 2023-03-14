#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntstarshipShareAcceptModel(object):

    def __init__(self):
        self._activity_id = None
        self._invite_date = None
        self._inviter_id = None
        self._sku_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def invite_date(self):
        return self._invite_date

    @invite_date.setter
    def invite_date(self, value):
        self._invite_date = value
    @property
    def inviter_id(self):
        return self._inviter_id

    @inviter_id.setter
    def inviter_id(self, value):
        self._inviter_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.invite_date:
            if hasattr(self.invite_date, 'to_alipay_dict'):
                params['invite_date'] = self.invite_date.to_alipay_dict()
            else:
                params['invite_date'] = self.invite_date
        if self.inviter_id:
            if hasattr(self.inviter_id, 'to_alipay_dict'):
                params['inviter_id'] = self.inviter_id.to_alipay_dict()
            else:
                params['inviter_id'] = self.inviter_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntstarshipShareAcceptModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'invite_date' in d:
            o.invite_date = d['invite_date']
        if 'inviter_id' in d:
            o.inviter_id = d['inviter_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


