#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubAccountQueryResult(object):

    def __init__(self):
        self._account_no = None
        self._alipay_virtual_id = None
        self._out_fin_inst_abbreviation = None
        self._source_uid = None
        self._status = None
        self._sub_account_no = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def alipay_virtual_id(self):
        return self._alipay_virtual_id

    @alipay_virtual_id.setter
    def alipay_virtual_id(self, value):
        self._alipay_virtual_id = value
    @property
    def out_fin_inst_abbreviation(self):
        return self._out_fin_inst_abbreviation

    @out_fin_inst_abbreviation.setter
    def out_fin_inst_abbreviation(self, value):
        self._out_fin_inst_abbreviation = value
    @property
    def source_uid(self):
        return self._source_uid

    @source_uid.setter
    def source_uid(self, value):
        self._source_uid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_account_no(self):
        return self._sub_account_no

    @sub_account_no.setter
    def sub_account_no(self, value):
        self._sub_account_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.alipay_virtual_id:
            if hasattr(self.alipay_virtual_id, 'to_alipay_dict'):
                params['alipay_virtual_id'] = self.alipay_virtual_id.to_alipay_dict()
            else:
                params['alipay_virtual_id'] = self.alipay_virtual_id
        if self.out_fin_inst_abbreviation:
            if hasattr(self.out_fin_inst_abbreviation, 'to_alipay_dict'):
                params['out_fin_inst_abbreviation'] = self.out_fin_inst_abbreviation.to_alipay_dict()
            else:
                params['out_fin_inst_abbreviation'] = self.out_fin_inst_abbreviation
        if self.source_uid:
            if hasattr(self.source_uid, 'to_alipay_dict'):
                params['source_uid'] = self.source_uid.to_alipay_dict()
            else:
                params['source_uid'] = self.source_uid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_account_no:
            if hasattr(self.sub_account_no, 'to_alipay_dict'):
                params['sub_account_no'] = self.sub_account_no.to_alipay_dict()
            else:
                params['sub_account_no'] = self.sub_account_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountQueryResult()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'alipay_virtual_id' in d:
            o.alipay_virtual_id = d['alipay_virtual_id']
        if 'out_fin_inst_abbreviation' in d:
            o.out_fin_inst_abbreviation = d['out_fin_inst_abbreviation']
        if 'source_uid' in d:
            o.source_uid = d['source_uid']
        if 'status' in d:
            o.status = d['status']
        if 'sub_account_no' in d:
            o.sub_account_no = d['sub_account_no']
        return o


