#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCommGroupInfo import KbdishCommGroupInfo


class KoubeiCateringDishCommgroupSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._kbdish_comm_group_info = None
        self._syn_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def kbdish_comm_group_info(self):
        return self._kbdish_comm_group_info

    @kbdish_comm_group_info.setter
    def kbdish_comm_group_info(self, value):
        if isinstance(value, KbdishCommGroupInfo):
            self._kbdish_comm_group_info = value
        else:
            self._kbdish_comm_group_info = KbdishCommGroupInfo.from_alipay_dict(value)
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.kbdish_comm_group_info:
            if hasattr(self.kbdish_comm_group_info, 'to_alipay_dict'):
                params['kbdish_comm_group_info'] = self.kbdish_comm_group_info.to_alipay_dict()
            else:
                params['kbdish_comm_group_info'] = self.kbdish_comm_group_info
        if self.syn_type:
            if hasattr(self.syn_type, 'to_alipay_dict'):
                params['syn_type'] = self.syn_type.to_alipay_dict()
            else:
                params['syn_type'] = self.syn_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCommgroupSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'kbdish_comm_group_info' in d:
            o.kbdish_comm_group_info = d['kbdish_comm_group_info']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


