#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetFundDTO import AssetFundDTO


class AlipayMarketingAssetFundRefundModel(object):

    def __init__(self):
        self._asset_fund_infos = None
        self._asset_id_type = None
        self._asset_type = None
        self._biz_dt = None
        self._biz_info = None
        self._biz_no = None
        self._fund_scene = None
        self._open_id = None
        self._use_order_id = None
        self._user_id = None

    @property
    def asset_fund_infos(self):
        return self._asset_fund_infos

    @asset_fund_infos.setter
    def asset_fund_infos(self, value):
        if isinstance(value, list):
            self._asset_fund_infos = list()
            for i in value:
                if isinstance(i, AssetFundDTO):
                    self._asset_fund_infos.append(i)
                else:
                    self._asset_fund_infos.append(AssetFundDTO.from_alipay_dict(i))
    @property
    def asset_id_type(self):
        return self._asset_id_type

    @asset_id_type.setter
    def asset_id_type(self, value):
        self._asset_id_type = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def fund_scene(self):
        return self._fund_scene

    @fund_scene.setter
    def fund_scene(self, value):
        self._fund_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def use_order_id(self):
        return self._use_order_id

    @use_order_id.setter
    def use_order_id(self, value):
        self._use_order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_fund_infos:
            if isinstance(self.asset_fund_infos, list):
                for i in range(0, len(self.asset_fund_infos)):
                    element = self.asset_fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.asset_fund_infos, 'to_alipay_dict'):
                params['asset_fund_infos'] = self.asset_fund_infos.to_alipay_dict()
            else:
                params['asset_fund_infos'] = self.asset_fund_infos
        if self.asset_id_type:
            if hasattr(self.asset_id_type, 'to_alipay_dict'):
                params['asset_id_type'] = self.asset_id_type.to_alipay_dict()
            else:
                params['asset_id_type'] = self.asset_id_type
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.fund_scene:
            if hasattr(self.fund_scene, 'to_alipay_dict'):
                params['fund_scene'] = self.fund_scene.to_alipay_dict()
            else:
                params['fund_scene'] = self.fund_scene
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.use_order_id:
            if hasattr(self.use_order_id, 'to_alipay_dict'):
                params['use_order_id'] = self.use_order_id.to_alipay_dict()
            else:
                params['use_order_id'] = self.use_order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingAssetFundRefundModel()
        if 'asset_fund_infos' in d:
            o.asset_fund_infos = d['asset_fund_infos']
        if 'asset_id_type' in d:
            o.asset_id_type = d['asset_id_type']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'fund_scene' in d:
            o.fund_scene = d['fund_scene']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'use_order_id' in d:
            o.use_order_id = d['use_order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


