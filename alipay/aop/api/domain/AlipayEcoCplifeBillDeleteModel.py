#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeBillDeleteModel(object):

    def __init__(self):
        self._bill_entry_id_list = None
        self._community_id = None

    @property
    def bill_entry_id_list(self):
        return self._bill_entry_id_list

    @bill_entry_id_list.setter
    def bill_entry_id_list(self, value):
        if isinstance(value, list):
            self._bill_entry_id_list = list()
            for i in value:
                self._bill_entry_id_list.append(i)
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_entry_id_list:
            if isinstance(self.bill_entry_id_list, list):
                for i in range(0, len(self.bill_entry_id_list)):
                    element = self.bill_entry_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_entry_id_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_entry_id_list, 'to_alipay_dict'):
                params['bill_entry_id_list'] = self.bill_entry_id_list.to_alipay_dict()
            else:
                params['bill_entry_id_list'] = self.bill_entry_id_list
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
        o = AlipayEcoCplifeBillDeleteModel()
        if 'bill_entry_id_list' in d:
            o.bill_entry_id_list = d['bill_entry_id_list']
        if 'community_id' in d:
            o.community_id = d['community_id']
        return o


