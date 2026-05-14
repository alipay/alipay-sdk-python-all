#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceCouponCreateResponseDTO(object):

    def __init__(self):
        self._id = None
        self._item_no = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleForceCouponCreateResponseDTO()
        if 'id' in d:
            o.id = d['id']
        if 'item_no' in d:
            o.item_no = d['item_no']
        return o


