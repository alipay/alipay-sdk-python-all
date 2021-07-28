#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAliyunbenefitRefundModel(object):

    def __init__(self):
        self._ext_json = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayUserAliyunbenefitRefundModel()
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


