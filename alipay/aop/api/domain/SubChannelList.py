#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetsDetailParams import AssetsDetailParams


class SubChannelList(object):

    def __init__(self):
        self._asset_id = None
        self._asset_type = None
        self._asset_type_code = None
        self._assets_detail_params = None
        self._available_amount = None
        self._close_error_code = None
        self._close_error_msg = None
        self._compatible_channel_index = None
        self._enable = None
        self._enough = None
        self._inst_id = None
        self._install_counts = None
        self._limit_amount = None
        self._logo = None
        self._name = None
        self._recommend_text = None
        self._recommend_tip = None
        self._signed = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def assets_detail_params(self):
        return self._assets_detail_params

    @assets_detail_params.setter
    def assets_detail_params(self, value):
        if isinstance(value, AssetsDetailParams):
            self._assets_detail_params = value
        else:
            self._assets_detail_params = AssetsDetailParams.from_alipay_dict(value)
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def close_error_code(self):
        return self._close_error_code

    @close_error_code.setter
    def close_error_code(self, value):
        self._close_error_code = value
    @property
    def close_error_msg(self):
        return self._close_error_msg

    @close_error_msg.setter
    def close_error_msg(self, value):
        self._close_error_msg = value
    @property
    def compatible_channel_index(self):
        return self._compatible_channel_index

    @compatible_channel_index.setter
    def compatible_channel_index(self, value):
        self._compatible_channel_index = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def enough(self):
        return self._enough

    @enough.setter
    def enough(self, value):
        self._enough = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def install_counts(self):
        return self._install_counts

    @install_counts.setter
    def install_counts(self, value):
        self._install_counts = value
    @property
    def limit_amount(self):
        return self._limit_amount

    @limit_amount.setter
    def limit_amount(self, value):
        self._limit_amount = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def recommend_text(self):
        return self._recommend_text

    @recommend_text.setter
    def recommend_text(self, value):
        self._recommend_text = value
    @property
    def recommend_tip(self):
        return self._recommend_tip

    @recommend_tip.setter
    def recommend_tip(self, value):
        self._recommend_tip = value
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.assets_detail_params:
            if hasattr(self.assets_detail_params, 'to_alipay_dict'):
                params['assets_detail_params'] = self.assets_detail_params.to_alipay_dict()
            else:
                params['assets_detail_params'] = self.assets_detail_params
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.close_error_code:
            if hasattr(self.close_error_code, 'to_alipay_dict'):
                params['close_error_code'] = self.close_error_code.to_alipay_dict()
            else:
                params['close_error_code'] = self.close_error_code
        if self.close_error_msg:
            if hasattr(self.close_error_msg, 'to_alipay_dict'):
                params['close_error_msg'] = self.close_error_msg.to_alipay_dict()
            else:
                params['close_error_msg'] = self.close_error_msg
        if self.compatible_channel_index:
            if hasattr(self.compatible_channel_index, 'to_alipay_dict'):
                params['compatible_channel_index'] = self.compatible_channel_index.to_alipay_dict()
            else:
                params['compatible_channel_index'] = self.compatible_channel_index
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.enough:
            if hasattr(self.enough, 'to_alipay_dict'):
                params['enough'] = self.enough.to_alipay_dict()
            else:
                params['enough'] = self.enough
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.install_counts:
            if hasattr(self.install_counts, 'to_alipay_dict'):
                params['install_counts'] = self.install_counts.to_alipay_dict()
            else:
                params['install_counts'] = self.install_counts
        if self.limit_amount:
            if hasattr(self.limit_amount, 'to_alipay_dict'):
                params['limit_amount'] = self.limit_amount.to_alipay_dict()
            else:
                params['limit_amount'] = self.limit_amount
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.recommend_text:
            if hasattr(self.recommend_text, 'to_alipay_dict'):
                params['recommend_text'] = self.recommend_text.to_alipay_dict()
            else:
                params['recommend_text'] = self.recommend_text
        if self.recommend_tip:
            if hasattr(self.recommend_tip, 'to_alipay_dict'):
                params['recommend_tip'] = self.recommend_tip.to_alipay_dict()
            else:
                params['recommend_tip'] = self.recommend_tip
        if self.signed:
            if hasattr(self.signed, 'to_alipay_dict'):
                params['signed'] = self.signed.to_alipay_dict()
            else:
                params['signed'] = self.signed
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubChannelList()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'assets_detail_params' in d:
            o.assets_detail_params = d['assets_detail_params']
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'close_error_code' in d:
            o.close_error_code = d['close_error_code']
        if 'close_error_msg' in d:
            o.close_error_msg = d['close_error_msg']
        if 'compatible_channel_index' in d:
            o.compatible_channel_index = d['compatible_channel_index']
        if 'enable' in d:
            o.enable = d['enable']
        if 'enough' in d:
            o.enough = d['enough']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'install_counts' in d:
            o.install_counts = d['install_counts']
        if 'limit_amount' in d:
            o.limit_amount = d['limit_amount']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'recommend_text' in d:
            o.recommend_text = d['recommend_text']
        if 'recommend_tip' in d:
            o.recommend_tip = d['recommend_tip']
        if 'signed' in d:
            o.signed = d['signed']
        return o


