#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUserquerybyuidQueryModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._query_ref_account = None
        self._query_role = None
        self._query_serve = None
        self._tnt_inst_id = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def query_ref_account(self):
        return self._query_ref_account

    @query_ref_account.setter
    def query_ref_account(self, value):
        self._query_ref_account = value
    @property
    def query_role(self):
        return self._query_role

    @query_role.setter
    def query_role(self, value):
        self._query_role = value
    @property
    def query_serve(self):
        return self._query_serve

    @query_serve.setter
    def query_serve(self, value):
        self._query_serve = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.query_ref_account:
            if hasattr(self.query_ref_account, 'to_alipay_dict'):
                params['query_ref_account'] = self.query_ref_account.to_alipay_dict()
            else:
                params['query_ref_account'] = self.query_ref_account
        if self.query_role:
            if hasattr(self.query_role, 'to_alipay_dict'):
                params['query_role'] = self.query_role.to_alipay_dict()
            else:
                params['query_role'] = self.query_role
        if self.query_serve:
            if hasattr(self.query_serve, 'to_alipay_dict'):
                params['query_serve'] = self.query_serve.to_alipay_dict()
            else:
                params['query_serve'] = self.query_serve
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceUserquerybyuidQueryModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'query_ref_account' in d:
            o.query_ref_account = d['query_ref_account']
        if 'query_role' in d:
            o.query_role = d['query_role']
        if 'query_serve' in d:
            o.query_serve = d['query_serve']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


