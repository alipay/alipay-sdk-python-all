#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DesignTextInfo import DesignTextInfo


class ItemDesignTextInfo(object):

    def __init__(self):
        self._design_text_info_list = None
        self._item_id = None

    @property
    def design_text_info_list(self):
        return self._design_text_info_list

    @design_text_info_list.setter
    def design_text_info_list(self, value):
        if isinstance(value, list):
            self._design_text_info_list = list()
            for i in value:
                if isinstance(i, DesignTextInfo):
                    self._design_text_info_list.append(i)
                else:
                    self._design_text_info_list.append(DesignTextInfo.from_alipay_dict(i))
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.design_text_info_list:
            if isinstance(self.design_text_info_list, list):
                for i in range(0, len(self.design_text_info_list)):
                    element = self.design_text_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.design_text_info_list[i] = element.to_alipay_dict()
            if hasattr(self.design_text_info_list, 'to_alipay_dict'):
                params['design_text_info_list'] = self.design_text_info_list.to_alipay_dict()
            else:
                params['design_text_info_list'] = self.design_text_info_list
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDesignTextInfo()
        if 'design_text_info_list' in d:
            o.design_text_info_list = d['design_text_info_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


