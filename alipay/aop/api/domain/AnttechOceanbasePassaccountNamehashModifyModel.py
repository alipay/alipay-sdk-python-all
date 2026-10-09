#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePassaccountNamehashModifyModel(object):

    def __init__(self):
        self._pass_account_id_list = None
        self._precheck = None
        self._snapshot_token = None

    @property
    def pass_account_id_list(self):
        return self._pass_account_id_list

    @pass_account_id_list.setter
    def pass_account_id_list(self, value):
        if isinstance(value, list):
            self._pass_account_id_list = list()
            for i in value:
                self._pass_account_id_list.append(i)
    @property
    def precheck(self):
        return self._precheck

    @precheck.setter
    def precheck(self, value):
        self._precheck = value
    @property
    def snapshot_token(self):
        return self._snapshot_token

    @snapshot_token.setter
    def snapshot_token(self, value):
        self._snapshot_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.pass_account_id_list:
            if isinstance(self.pass_account_id_list, list):
                for i in range(0, len(self.pass_account_id_list)):
                    element = self.pass_account_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pass_account_id_list[i] = element.to_alipay_dict()
            if hasattr(self.pass_account_id_list, 'to_alipay_dict'):
                params['pass_account_id_list'] = self.pass_account_id_list.to_alipay_dict()
            else:
                params['pass_account_id_list'] = self.pass_account_id_list
        if self.precheck:
            if hasattr(self.precheck, 'to_alipay_dict'):
                params['precheck'] = self.precheck.to_alipay_dict()
            else:
                params['precheck'] = self.precheck
        if self.snapshot_token:
            if hasattr(self.snapshot_token, 'to_alipay_dict'):
                params['snapshot_token'] = self.snapshot_token.to_alipay_dict()
            else:
                params['snapshot_token'] = self.snapshot_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbasePassaccountNamehashModifyModel()
        if 'pass_account_id_list' in d:
            o.pass_account_id_list = d['pass_account_id_list']
        if 'precheck' in d:
            o.precheck = d['precheck']
        if 'snapshot_token' in d:
            o.snapshot_token = d['snapshot_token']
        return o


