#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingToolMallPointsSyncModel(object):

    def __init__(self):
        self._activity_id = None
        self._biz_type = None
        self._gmt_end = None
        self._json_content = None
        self._mall_id = None
        self._operate = None
        self._out_biz_id = None
        self._state = None
        self._trade_id = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def json_content(self):
        return self._json_content

    @json_content.setter
    def json_content(self, value):
        self._json_content = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.json_content:
            if hasattr(self.json_content, 'to_alipay_dict'):
                params['json_content'] = self.json_content.to_alipay_dict()
            else:
                params['json_content'] = self.json_content
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
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
        o = KoubeiMarketingToolMallPointsSyncModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'json_content' in d:
            o.json_content = d['json_content']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'operate' in d:
            o.operate = d['operate']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'state' in d:
            o.state = d['state']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


