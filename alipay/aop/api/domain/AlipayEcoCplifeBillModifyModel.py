#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CPBillModifySet import CPBillModifySet


class AlipayEcoCplifeBillModifyModel(object):

    def __init__(self):
        self._bill_entry_list = None
        self._community_id = None

    @property
    def bill_entry_list(self):
        return self._bill_entry_list

    @bill_entry_list.setter
    def bill_entry_list(self, value):
        if isinstance(value, list):
            self._bill_entry_list = list()
            for i in value:
                if isinstance(i, CPBillModifySet):
                    self._bill_entry_list.append(i)
                else:
                    self._bill_entry_list.append(CPBillModifySet.from_alipay_dict(i))
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_entry_list:
            if isinstance(self.bill_entry_list, list):
                for i in range(0, len(self.bill_entry_list)):
                    element = self.bill_entry_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_entry_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_entry_list, 'to_alipay_dict'):
                params['bill_entry_list'] = self.bill_entry_list.to_alipay_dict()
            else:
                params['bill_entry_list'] = self.bill_entry_list
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeBillModifyModel()
        if 'bill_entry_list' in d:
            o.bill_entry_list = d['bill_entry_list']
        if 'community_id' in d:
            o.community_id = d['community_id']
        return o


