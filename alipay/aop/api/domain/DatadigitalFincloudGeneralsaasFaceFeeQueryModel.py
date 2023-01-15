#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasFaceFeeQueryModel(object):

    def __init__(self):
        self._certify_id_list = None

    @property
    def certify_id_list(self):
        return self._certify_id_list

    @certify_id_list.setter
    def certify_id_list(self, value):
        if isinstance(value, list):
            self._certify_id_list = list()
            for i in value:
                self._certify_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.certify_id_list:
            if isinstance(self.certify_id_list, list):
                for i in range(0, len(self.certify_id_list)):
                    element = self.certify_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certify_id_list[i] = element.to_alipay_dict()
            if hasattr(self.certify_id_list, 'to_alipay_dict'):
                params['certify_id_list'] = self.certify_id_list.to_alipay_dict()
            else:
                params['certify_id_list'] = self.certify_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasFaceFeeQueryModel()
        if 'certify_id_list' in d:
            o.certify_id_list = d['certify_id_list']
        return o


