#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StandardBailDTO(object):

    def __init__(self):
        self._amount = None
        self._bail_status = None
        self._gmt_create = None
        self._gmt_modified = None
        self._migrate_to = None
        self._partner_user_id = None
        self._scene_desc = None
        self._type_code = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bail_status(self):
        return self._bail_status

    @bail_status.setter
    def bail_status(self, value):
        self._bail_status = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def migrate_to(self):
        return self._migrate_to

    @migrate_to.setter
    def migrate_to(self, value):
        self._migrate_to = value
    @property
    def partner_user_id(self):
        return self._partner_user_id

    @partner_user_id.setter
    def partner_user_id(self, value):
        self._partner_user_id = value
    @property
    def scene_desc(self):
        return self._scene_desc

    @scene_desc.setter
    def scene_desc(self, value):
        self._scene_desc = value
    @property
    def type_code(self):
        return self._type_code

    @type_code.setter
    def type_code(self, value):
        self._type_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bail_status:
            if hasattr(self.bail_status, 'to_alipay_dict'):
                params['bail_status'] = self.bail_status.to_alipay_dict()
            else:
                params['bail_status'] = self.bail_status
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.migrate_to:
            if hasattr(self.migrate_to, 'to_alipay_dict'):
                params['migrate_to'] = self.migrate_to.to_alipay_dict()
            else:
                params['migrate_to'] = self.migrate_to
        if self.partner_user_id:
            if hasattr(self.partner_user_id, 'to_alipay_dict'):
                params['partner_user_id'] = self.partner_user_id.to_alipay_dict()
            else:
                params['partner_user_id'] = self.partner_user_id
        if self.scene_desc:
            if hasattr(self.scene_desc, 'to_alipay_dict'):
                params['scene_desc'] = self.scene_desc.to_alipay_dict()
            else:
                params['scene_desc'] = self.scene_desc
        if self.type_code:
            if hasattr(self.type_code, 'to_alipay_dict'):
                params['type_code'] = self.type_code.to_alipay_dict()
            else:
                params['type_code'] = self.type_code
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
        o = StandardBailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bail_status' in d:
            o.bail_status = d['bail_status']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'migrate_to' in d:
            o.migrate_to = d['migrate_to']
        if 'partner_user_id' in d:
            o.partner_user_id = d['partner_user_id']
        if 'scene_desc' in d:
            o.scene_desc = d['scene_desc']
        if 'type_code' in d:
            o.type_code = d['type_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


