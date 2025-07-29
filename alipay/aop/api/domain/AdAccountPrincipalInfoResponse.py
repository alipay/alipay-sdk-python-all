#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdAccountPrincipalInfoResponse(object):

    def __init__(self):
        self._alipay_account = None
        self._alipay_oid = None
        self._first_trade_id = None
        self._first_trade_name = None
        self._gmt_create = None
        self._principal_id = None
        self._principal_name = None
        self._second_trade_id = None
        self._second_trade_name = None
        self._status = None
        self._status_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def alipay_oid(self):
        return self._alipay_oid

    @alipay_oid.setter
    def alipay_oid(self, value):
        self._alipay_oid = value
    @property
    def first_trade_id(self):
        return self._first_trade_id

    @first_trade_id.setter
    def first_trade_id(self, value):
        self._first_trade_id = value
    @property
    def first_trade_name(self):
        return self._first_trade_name

    @first_trade_name.setter
    def first_trade_name(self, value):
        self._first_trade_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value
    @property
    def second_trade_id(self):
        return self._second_trade_id

    @second_trade_id.setter
    def second_trade_id(self, value):
        self._second_trade_id = value
    @property
    def second_trade_name(self):
        return self._second_trade_name

    @second_trade_name.setter
    def second_trade_name(self, value):
        self._second_trade_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.alipay_oid:
            if hasattr(self.alipay_oid, 'to_alipay_dict'):
                params['alipay_oid'] = self.alipay_oid.to_alipay_dict()
            else:
                params['alipay_oid'] = self.alipay_oid
        if self.first_trade_id:
            if hasattr(self.first_trade_id, 'to_alipay_dict'):
                params['first_trade_id'] = self.first_trade_id.to_alipay_dict()
            else:
                params['first_trade_id'] = self.first_trade_id
        if self.first_trade_name:
            if hasattr(self.first_trade_name, 'to_alipay_dict'):
                params['first_trade_name'] = self.first_trade_name.to_alipay_dict()
            else:
                params['first_trade_name'] = self.first_trade_name
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
        if self.second_trade_id:
            if hasattr(self.second_trade_id, 'to_alipay_dict'):
                params['second_trade_id'] = self.second_trade_id.to_alipay_dict()
            else:
                params['second_trade_id'] = self.second_trade_id
        if self.second_trade_name:
            if hasattr(self.second_trade_name, 'to_alipay_dict'):
                params['second_trade_name'] = self.second_trade_name.to_alipay_dict()
            else:
                params['second_trade_name'] = self.second_trade_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_name:
            if hasattr(self.status_name, 'to_alipay_dict'):
                params['status_name'] = self.status_name.to_alipay_dict()
            else:
                params['status_name'] = self.status_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdAccountPrincipalInfoResponse()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'alipay_oid' in d:
            o.alipay_oid = d['alipay_oid']
        if 'first_trade_id' in d:
            o.first_trade_id = d['first_trade_id']
        if 'first_trade_name' in d:
            o.first_trade_name = d['first_trade_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'second_trade_id' in d:
            o.second_trade_id = d['second_trade_id']
        if 'second_trade_name' in d:
            o.second_trade_name = d['second_trade_name']
        if 'status' in d:
            o.status = d['status']
        if 'status_name' in d:
            o.status_name = d['status_name']
        return o


