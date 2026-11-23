#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OwnerWhiteVO(object):

    def __init__(self):
        self._delete_flag = None
        self._owner_id = None

    @property
    def delete_flag(self):
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, value):
        self._delete_flag = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_flag:
            if hasattr(self.delete_flag, 'to_alipay_dict'):
                params['delete_flag'] = self.delete_flag.to_alipay_dict()
            else:
                params['delete_flag'] = self.delete_flag
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OwnerWhiteVO()
        if 'delete_flag' in d:
            o.delete_flag = d['delete_flag']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        return o


