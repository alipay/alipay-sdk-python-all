#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdConversionJoinWindow import AdConversionJoinWindow


class AdConversion(object):

    def __init__(self):
        self._asset_type_code = None
        self._asset_type_name = None
        self._conversion_id = None
        self._conversion_name_show = None
        self._conversion_raw_data_type_name = None
        self._conversion_type_code = None
        self._conversion_type_name = None
        self._gmt_modified = None
        self._join_window_name = None

    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def asset_type_name(self):
        return self._asset_type_name

    @asset_type_name.setter
    def asset_type_name(self, value):
        self._asset_type_name = value
    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def conversion_name_show(self):
        return self._conversion_name_show

    @conversion_name_show.setter
    def conversion_name_show(self, value):
        self._conversion_name_show = value
    @property
    def conversion_raw_data_type_name(self):
        return self._conversion_raw_data_type_name

    @conversion_raw_data_type_name.setter
    def conversion_raw_data_type_name(self, value):
        self._conversion_raw_data_type_name = value
    @property
    def conversion_type_code(self):
        return self._conversion_type_code

    @conversion_type_code.setter
    def conversion_type_code(self, value):
        self._conversion_type_code = value
    @property
    def conversion_type_name(self):
        return self._conversion_type_name

    @conversion_type_name.setter
    def conversion_type_name(self, value):
        self._conversion_type_name = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def join_window_name(self):
        return self._join_window_name

    @join_window_name.setter
    def join_window_name(self, value):
        if isinstance(value, AdConversionJoinWindow):
            self._join_window_name = value
        else:
            self._join_window_name = AdConversionJoinWindow.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.asset_type_name:
            if hasattr(self.asset_type_name, 'to_alipay_dict'):
                params['asset_type_name'] = self.asset_type_name.to_alipay_dict()
            else:
                params['asset_type_name'] = self.asset_type_name
        if self.conversion_id:
            if hasattr(self.conversion_id, 'to_alipay_dict'):
                params['conversion_id'] = self.conversion_id.to_alipay_dict()
            else:
                params['conversion_id'] = self.conversion_id
        if self.conversion_name_show:
            if hasattr(self.conversion_name_show, 'to_alipay_dict'):
                params['conversion_name_show'] = self.conversion_name_show.to_alipay_dict()
            else:
                params['conversion_name_show'] = self.conversion_name_show
        if self.conversion_raw_data_type_name:
            if hasattr(self.conversion_raw_data_type_name, 'to_alipay_dict'):
                params['conversion_raw_data_type_name'] = self.conversion_raw_data_type_name.to_alipay_dict()
            else:
                params['conversion_raw_data_type_name'] = self.conversion_raw_data_type_name
        if self.conversion_type_code:
            if hasattr(self.conversion_type_code, 'to_alipay_dict'):
                params['conversion_type_code'] = self.conversion_type_code.to_alipay_dict()
            else:
                params['conversion_type_code'] = self.conversion_type_code
        if self.conversion_type_name:
            if hasattr(self.conversion_type_name, 'to_alipay_dict'):
                params['conversion_type_name'] = self.conversion_type_name.to_alipay_dict()
            else:
                params['conversion_type_name'] = self.conversion_type_name
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.join_window_name:
            if hasattr(self.join_window_name, 'to_alipay_dict'):
                params['join_window_name'] = self.join_window_name.to_alipay_dict()
            else:
                params['join_window_name'] = self.join_window_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdConversion()
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'asset_type_name' in d:
            o.asset_type_name = d['asset_type_name']
        if 'conversion_id' in d:
            o.conversion_id = d['conversion_id']
        if 'conversion_name_show' in d:
            o.conversion_name_show = d['conversion_name_show']
        if 'conversion_raw_data_type_name' in d:
            o.conversion_raw_data_type_name = d['conversion_raw_data_type_name']
        if 'conversion_type_code' in d:
            o.conversion_type_code = d['conversion_type_code']
        if 'conversion_type_name' in d:
            o.conversion_type_name = d['conversion_type_name']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'join_window_name' in d:
            o.join_window_name = d['join_window_name']
        return o


