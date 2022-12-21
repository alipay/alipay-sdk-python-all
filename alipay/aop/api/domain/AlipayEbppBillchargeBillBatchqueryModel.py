#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillKeyInfo import BillKeyInfo


class AlipayEbppBillchargeBillBatchqueryModel(object):

    def __init__(self):
        self._billkey_list = None
        self._open_id = None
        self._source = None
        self._user_id = None

    @property
    def billkey_list(self):
        return self._billkey_list

    @billkey_list.setter
    def billkey_list(self, value):
        if isinstance(value, list):
            self._billkey_list = list()
            for i in value:
                if isinstance(i, BillKeyInfo):
                    self._billkey_list.append(i)
                else:
                    self._billkey_list.append(BillKeyInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.billkey_list:
            if isinstance(self.billkey_list, list):
                for i in range(0, len(self.billkey_list)):
                    element = self.billkey_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.billkey_list[i] = element.to_alipay_dict()
            if hasattr(self.billkey_list, 'to_alipay_dict'):
                params['billkey_list'] = self.billkey_list.to_alipay_dict()
            else:
                params['billkey_list'] = self.billkey_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayEbppBillchargeBillBatchqueryModel()
        if 'billkey_list' in d:
            o.billkey_list = d['billkey_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


