#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConvertedEventGrpDetail import ConvertedEventGrpDetail


class AssetDetail(object):

    def __init__(self):
        self._asset = None
        self._asset_name = None
        self._converted_event_grp_detail_list = None

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value
    @property
    def asset_name(self):
        return self._asset_name

    @asset_name.setter
    def asset_name(self, value):
        self._asset_name = value
    @property
    def converted_event_grp_detail_list(self):
        return self._converted_event_grp_detail_list

    @converted_event_grp_detail_list.setter
    def converted_event_grp_detail_list(self, value):
        if isinstance(value, list):
            self._converted_event_grp_detail_list = list()
            for i in value:
                if isinstance(i, ConvertedEventGrpDetail):
                    self._converted_event_grp_detail_list.append(i)
                else:
                    self._converted_event_grp_detail_list.append(ConvertedEventGrpDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset:
            if hasattr(self.asset, 'to_alipay_dict'):
                params['asset'] = self.asset.to_alipay_dict()
            else:
                params['asset'] = self.asset
        if self.asset_name:
            if hasattr(self.asset_name, 'to_alipay_dict'):
                params['asset_name'] = self.asset_name.to_alipay_dict()
            else:
                params['asset_name'] = self.asset_name
        if self.converted_event_grp_detail_list:
            if isinstance(self.converted_event_grp_detail_list, list):
                for i in range(0, len(self.converted_event_grp_detail_list)):
                    element = self.converted_event_grp_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.converted_event_grp_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.converted_event_grp_detail_list, 'to_alipay_dict'):
                params['converted_event_grp_detail_list'] = self.converted_event_grp_detail_list.to_alipay_dict()
            else:
                params['converted_event_grp_detail_list'] = self.converted_event_grp_detail_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetDetail()
        if 'asset' in d:
            o.asset = d['asset']
        if 'asset_name' in d:
            o.asset_name = d['asset_name']
        if 'converted_event_grp_detail_list' in d:
            o.converted_event_grp_detail_list = d['converted_event_grp_detail_list']
        return o


