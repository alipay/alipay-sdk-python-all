#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMemberInfoSyncModel(object):

    def __init__(self):
        self._card_id = None
        self._closed = None
        self._issuance_date = None
        self._occur_time = None
        self._open_date = None
        self._open_id = None
        self._operator_uid = None
        self._purchase_time = None
        self._scene_id = None
        self._user_id = None
        self._valid_date = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def closed(self):
        return self._closed

    @closed.setter
    def closed(self, value):
        self._closed = value
    @property
    def issuance_date(self):
        return self._issuance_date

    @issuance_date.setter
    def issuance_date(self, value):
        self._issuance_date = value
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, value):
        self._open_date = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def purchase_time(self):
        return self._purchase_time

    @purchase_time.setter
    def purchase_time(self, value):
        self._purchase_time = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.closed:
            if hasattr(self.closed, 'to_alipay_dict'):
                params['closed'] = self.closed.to_alipay_dict()
            else:
                params['closed'] = self.closed
        if self.issuance_date:
            if hasattr(self.issuance_date, 'to_alipay_dict'):
                params['issuance_date'] = self.issuance_date.to_alipay_dict()
            else:
                params['issuance_date'] = self.issuance_date
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.open_date:
            if hasattr(self.open_date, 'to_alipay_dict'):
                params['open_date'] = self.open_date.to_alipay_dict()
            else:
                params['open_date'] = self.open_date
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.purchase_time:
            if hasattr(self.purchase_time, 'to_alipay_dict'):
                params['purchase_time'] = self.purchase_time.to_alipay_dict()
            else:
                params['purchase_time'] = self.purchase_time
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarMemberInfoSyncModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'closed' in d:
            o.closed = d['closed']
        if 'issuance_date' in d:
            o.issuance_date = d['issuance_date']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'open_date' in d:
            o.open_date = d['open_date']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'purchase_time' in d:
            o.purchase_time = d['purchase_time']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


