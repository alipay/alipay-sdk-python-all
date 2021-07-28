#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FliggyPoiInfo(object):

    def __init__(self):
        self._biz_code = None
        self._msg = None
        self._poi_id = None
        self._success = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FliggyPoiInfo()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'msg' in d:
            o.msg = d['msg']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'success' in d:
            o.success = d['success']
        return o


