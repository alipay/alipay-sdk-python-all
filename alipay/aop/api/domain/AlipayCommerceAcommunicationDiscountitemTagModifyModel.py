#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDiscountitemTagModifyModel(object):

    def __init__(self):
        self._isv_item_id = None
        self._tag_code_list = None

    @property
    def isv_item_id(self):
        return self._isv_item_id

    @isv_item_id.setter
    def isv_item_id(self, value):
        self._isv_item_id = value
    @property
    def tag_code_list(self):
        return self._tag_code_list

    @tag_code_list.setter
    def tag_code_list(self, value):
        self._tag_code_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_item_id:
            if hasattr(self.isv_item_id, 'to_alipay_dict'):
                params['isv_item_id'] = self.isv_item_id.to_alipay_dict()
            else:
                params['isv_item_id'] = self.isv_item_id
        if self.tag_code_list:
            if hasattr(self.tag_code_list, 'to_alipay_dict'):
                params['tag_code_list'] = self.tag_code_list.to_alipay_dict()
            else:
                params['tag_code_list'] = self.tag_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDiscountitemTagModifyModel()
        if 'isv_item_id' in d:
            o.isv_item_id = d['isv_item_id']
        if 'tag_code_list' in d:
            o.tag_code_list = d['tag_code_list']
        return o


