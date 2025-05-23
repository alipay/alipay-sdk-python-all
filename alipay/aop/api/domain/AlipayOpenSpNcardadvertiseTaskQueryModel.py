#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNcardadvertiseTaskQueryModel(object):

    def __init__(self):
        self._tag_id_list = None

    @property
    def tag_id_list(self):
        return self._tag_id_list

    @tag_id_list.setter
    def tag_id_list(self, value):
        if isinstance(value, list):
            self._tag_id_list = list()
            for i in value:
                self._tag_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.tag_id_list:
            if isinstance(self.tag_id_list, list):
                for i in range(0, len(self.tag_id_list)):
                    element = self.tag_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_id_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_id_list, 'to_alipay_dict'):
                params['tag_id_list'] = self.tag_id_list.to_alipay_dict()
            else:
                params['tag_id_list'] = self.tag_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNcardadvertiseTaskQueryModel()
        if 'tag_id_list' in d:
            o.tag_id_list = d['tag_id_list']
        return o


