#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppFamilyShareSyncModel(object):

    def __init__(self):
        self._open_id = None
        self._share_expired = None
        self._share_open_id = None
        self._share_sku_expired = None
        self._share_target = None
        self._share_target_expire = None
        self._share_target_type = None
        self._share_uid = None
        self._sku = None
        self._status = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def share_expired(self):
        return self._share_expired

    @share_expired.setter
    def share_expired(self, value):
        self._share_expired = value
    @property
    def share_open_id(self):
        return self._share_open_id

    @share_open_id.setter
    def share_open_id(self, value):
        self._share_open_id = value
    @property
    def share_sku_expired(self):
        return self._share_sku_expired

    @share_sku_expired.setter
    def share_sku_expired(self, value):
        self._share_sku_expired = value
    @property
    def share_target(self):
        return self._share_target

    @share_target.setter
    def share_target(self, value):
        self._share_target = value
    @property
    def share_target_expire(self):
        return self._share_target_expire

    @share_target_expire.setter
    def share_target_expire(self, value):
        self._share_target_expire = value
    @property
    def share_target_type(self):
        return self._share_target_type

    @share_target_type.setter
    def share_target_type(self, value):
        self._share_target_type = value
    @property
    def share_uid(self):
        return self._share_uid

    @share_uid.setter
    def share_uid(self, value):
        self._share_uid = value
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.share_expired:
            if hasattr(self.share_expired, 'to_alipay_dict'):
                params['share_expired'] = self.share_expired.to_alipay_dict()
            else:
                params['share_expired'] = self.share_expired
        if self.share_open_id:
            if hasattr(self.share_open_id, 'to_alipay_dict'):
                params['share_open_id'] = self.share_open_id.to_alipay_dict()
            else:
                params['share_open_id'] = self.share_open_id
        if self.share_sku_expired:
            if hasattr(self.share_sku_expired, 'to_alipay_dict'):
                params['share_sku_expired'] = self.share_sku_expired.to_alipay_dict()
            else:
                params['share_sku_expired'] = self.share_sku_expired
        if self.share_target:
            if hasattr(self.share_target, 'to_alipay_dict'):
                params['share_target'] = self.share_target.to_alipay_dict()
            else:
                params['share_target'] = self.share_target
        if self.share_target_expire:
            if hasattr(self.share_target_expire, 'to_alipay_dict'):
                params['share_target_expire'] = self.share_target_expire.to_alipay_dict()
            else:
                params['share_target_expire'] = self.share_target_expire
        if self.share_target_type:
            if hasattr(self.share_target_type, 'to_alipay_dict'):
                params['share_target_type'] = self.share_target_type.to_alipay_dict()
            else:
                params['share_target_type'] = self.share_target_type
        if self.share_uid:
            if hasattr(self.share_uid, 'to_alipay_dict'):
                params['share_uid'] = self.share_uid.to_alipay_dict()
            else:
                params['share_uid'] = self.share_uid
        if self.sku:
            if hasattr(self.sku, 'to_alipay_dict'):
                params['sku'] = self.sku.to_alipay_dict()
            else:
                params['sku'] = self.sku
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppFamilyShareSyncModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'share_expired' in d:
            o.share_expired = d['share_expired']
        if 'share_open_id' in d:
            o.share_open_id = d['share_open_id']
        if 'share_sku_expired' in d:
            o.share_sku_expired = d['share_sku_expired']
        if 'share_target' in d:
            o.share_target = d['share_target']
        if 'share_target_expire' in d:
            o.share_target_expire = d['share_target_expire']
        if 'share_target_type' in d:
            o.share_target_type = d['share_target_type']
        if 'share_uid' in d:
            o.share_uid = d['share_uid']
        if 'sku' in d:
            o.sku = d['sku']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


