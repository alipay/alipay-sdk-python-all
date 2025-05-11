#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BFActivityFundInfo import BFActivityFundInfo


class BFActivityFundInfoNew(object):

    def __init__(self):
        self._asset_type = None
        self._fund_info_list = None
        self._inst_id = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def fund_info_list(self):
        return self._fund_info_list

    @fund_info_list.setter
    def fund_info_list(self, value):
        if isinstance(value, list):
            self._fund_info_list = list()
            for i in value:
                if isinstance(i, BFActivityFundInfo):
                    self._fund_info_list.append(i)
                else:
                    self._fund_info_list.append(BFActivityFundInfo.from_alipay_dict(i))
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.fund_info_list:
            if isinstance(self.fund_info_list, list):
                for i in range(0, len(self.fund_info_list)):
                    element = self.fund_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_info_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_info_list, 'to_alipay_dict'):
                params['fund_info_list'] = self.fund_info_list.to_alipay_dict()
            else:
                params['fund_info_list'] = self.fund_info_list
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BFActivityFundInfoNew()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'fund_info_list' in d:
            o.fund_info_list = d['fund_info_list']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        return o


