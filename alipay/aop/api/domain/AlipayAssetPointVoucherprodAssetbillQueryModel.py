#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointVoucherprodAssetbillQueryModel(object):

    def __init__(self):
        self._asset_id = None
        self._asset_type = None
        self._biz_no = None
        self._biz_type = None
        self._end_biz_dt = None
        self._page_num = None
        self._page_size = None
        self._start_biz_dt = None
        self._user_id = None

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
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def end_biz_dt(self):
        return self._end_biz_dt

    @end_biz_dt.setter
    def end_biz_dt(self, value):
        self._end_biz_dt = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start_biz_dt(self):
        return self._start_biz_dt

    @start_biz_dt.setter
    def start_biz_dt(self, value):
        self._start_biz_dt = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.end_biz_dt:
            if hasattr(self.end_biz_dt, 'to_alipay_dict'):
                params['end_biz_dt'] = self.end_biz_dt.to_alipay_dict()
            else:
                params['end_biz_dt'] = self.end_biz_dt
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start_biz_dt:
            if hasattr(self.start_biz_dt, 'to_alipay_dict'):
                params['start_biz_dt'] = self.start_biz_dt.to_alipay_dict()
            else:
                params['start_biz_dt'] = self.start_biz_dt
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
        o = AlipayAssetPointVoucherprodAssetbillQueryModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_biz_dt' in d:
            o.end_biz_dt = d['end_biz_dt']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_biz_dt' in d:
            o.start_biz_dt = d['start_biz_dt']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


