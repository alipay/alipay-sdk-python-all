#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountInfoVO(object):

    def __init__(self):
        self._account_alias_name = None
        self._account_name = None
        self._account_nature = None
        self._account_no = None
        self._account_type = None
        self._account_user_id = None
        self._inst_id = None
        self._inst_name = None
        self._out_inst_abbr = None
        self._out_inst_name = None
        self._parent_inst_id = None
        self._sub_account_no = None
        self._sub_account_type = None
        self._tnt_inst_id = None

    @property
    def account_alias_name(self):
        return self._account_alias_name

    @account_alias_name.setter
    def account_alias_name(self, value):
        self._account_alias_name = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_nature(self):
        return self._account_nature

    @account_nature.setter
    def account_nature(self, value):
        self._account_nature = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def account_user_id(self):
        return self._account_user_id

    @account_user_id.setter
    def account_user_id(self, value):
        self._account_user_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def out_inst_abbr(self):
        return self._out_inst_abbr

    @out_inst_abbr.setter
    def out_inst_abbr(self, value):
        self._out_inst_abbr = value
    @property
    def out_inst_name(self):
        return self._out_inst_name

    @out_inst_name.setter
    def out_inst_name(self, value):
        self._out_inst_name = value
    @property
    def parent_inst_id(self):
        return self._parent_inst_id

    @parent_inst_id.setter
    def parent_inst_id(self, value):
        self._parent_inst_id = value
    @property
    def sub_account_no(self):
        return self._sub_account_no

    @sub_account_no.setter
    def sub_account_no(self, value):
        self._sub_account_no = value
    @property
    def sub_account_type(self):
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, value):
        self._sub_account_type = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_alias_name:
            if hasattr(self.account_alias_name, 'to_alipay_dict'):
                params['account_alias_name'] = self.account_alias_name.to_alipay_dict()
            else:
                params['account_alias_name'] = self.account_alias_name
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_nature:
            if hasattr(self.account_nature, 'to_alipay_dict'):
                params['account_nature'] = self.account_nature.to_alipay_dict()
            else:
                params['account_nature'] = self.account_nature
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.account_user_id:
            if hasattr(self.account_user_id, 'to_alipay_dict'):
                params['account_user_id'] = self.account_user_id.to_alipay_dict()
            else:
                params['account_user_id'] = self.account_user_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.out_inst_abbr:
            if hasattr(self.out_inst_abbr, 'to_alipay_dict'):
                params['out_inst_abbr'] = self.out_inst_abbr.to_alipay_dict()
            else:
                params['out_inst_abbr'] = self.out_inst_abbr
        if self.out_inst_name:
            if hasattr(self.out_inst_name, 'to_alipay_dict'):
                params['out_inst_name'] = self.out_inst_name.to_alipay_dict()
            else:
                params['out_inst_name'] = self.out_inst_name
        if self.parent_inst_id:
            if hasattr(self.parent_inst_id, 'to_alipay_dict'):
                params['parent_inst_id'] = self.parent_inst_id.to_alipay_dict()
            else:
                params['parent_inst_id'] = self.parent_inst_id
        if self.sub_account_no:
            if hasattr(self.sub_account_no, 'to_alipay_dict'):
                params['sub_account_no'] = self.sub_account_no.to_alipay_dict()
            else:
                params['sub_account_no'] = self.sub_account_no
        if self.sub_account_type:
            if hasattr(self.sub_account_type, 'to_alipay_dict'):
                params['sub_account_type'] = self.sub_account_type.to_alipay_dict()
            else:
                params['sub_account_type'] = self.sub_account_type
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
        o = AccountInfoVO()
        if 'account_alias_name' in d:
            o.account_alias_name = d['account_alias_name']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_nature' in d:
            o.account_nature = d['account_nature']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'account_user_id' in d:
            o.account_user_id = d['account_user_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'out_inst_abbr' in d:
            o.out_inst_abbr = d['out_inst_abbr']
        if 'out_inst_name' in d:
            o.out_inst_name = d['out_inst_name']
        if 'parent_inst_id' in d:
            o.parent_inst_id = d['parent_inst_id']
        if 'sub_account_no' in d:
            o.sub_account_no = d['sub_account_no']
        if 'sub_account_type' in d:
            o.sub_account_type = d['sub_account_type']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


