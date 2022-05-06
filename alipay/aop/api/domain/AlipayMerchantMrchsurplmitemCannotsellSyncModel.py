#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantMrchsurplmitemCannotsellSyncModel(object):

    def __init__(self):
        self._biz_id = None
        self._ext_info = None
        self._item_id = None
        self._notice_time = None
        self._notice_type = None
        self._request_id = None
        self._sub_biz_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def notice_time(self):
        return self._notice_time

    @notice_time.setter
    def notice_time(self, value):
        self._notice_time = value
    @property
    def notice_type(self):
        return self._notice_type

    @notice_type.setter
    def notice_type(self, value):
        self._notice_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sub_biz_id(self):
        return self._sub_biz_id

    @sub_biz_id.setter
    def sub_biz_id(self, value):
        self._sub_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.notice_time:
            if hasattr(self.notice_time, 'to_alipay_dict'):
                params['notice_time'] = self.notice_time.to_alipay_dict()
            else:
                params['notice_time'] = self.notice_time
        if self.notice_type:
            if hasattr(self.notice_type, 'to_alipay_dict'):
                params['notice_type'] = self.notice_type.to_alipay_dict()
            else:
                params['notice_type'] = self.notice_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sub_biz_id:
            if hasattr(self.sub_biz_id, 'to_alipay_dict'):
                params['sub_biz_id'] = self.sub_biz_id.to_alipay_dict()
            else:
                params['sub_biz_id'] = self.sub_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantMrchsurplmitemCannotsellSyncModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'notice_time' in d:
            o.notice_time = d['notice_time']
        if 'notice_type' in d:
            o.notice_type = d['notice_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sub_biz_id' in d:
            o.sub_biz_id = d['sub_biz_id']
        return o


