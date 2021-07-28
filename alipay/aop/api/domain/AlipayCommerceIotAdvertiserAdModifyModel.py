#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotAdvertiserAdModifyModel(object):

    def __init__(self):
        self._delete_sn_list = None
        self._id = None

    @property
    def delete_sn_list(self):
        return self._delete_sn_list

    @delete_sn_list.setter
    def delete_sn_list(self, value):
        if isinstance(value, list):
            self._delete_sn_list = list()
            for i in value:
                self._delete_sn_list.append(i)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_sn_list:
            if isinstance(self.delete_sn_list, list):
                for i in range(0, len(self.delete_sn_list)):
                    element = self.delete_sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delete_sn_list[i] = element.to_alipay_dict()
            if hasattr(self.delete_sn_list, 'to_alipay_dict'):
                params['delete_sn_list'] = self.delete_sn_list.to_alipay_dict()
            else:
                params['delete_sn_list'] = self.delete_sn_list
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotAdvertiserAdModifyModel()
        if 'delete_sn_list' in d:
            o.delete_sn_list = d['delete_sn_list']
        if 'id' in d:
            o.id = d['id']
        return o


