#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenDataItemRecommendBatchqueryModel(object):

    def __init__(self):
        self._area_code = None
        self._ext_info = None
        self._position_ids = None
        self._user_id = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def position_ids(self):
        return self._position_ids

    @position_ids.setter
    def position_ids(self, value):
        self._position_ids = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.position_ids:
            if hasattr(self.position_ids, 'to_alipay_dict'):
                params['position_ids'] = self.position_ids.to_alipay_dict()
            else:
                params['position_ids'] = self.position_ids
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
        o = AlipayOpenDataItemRecommendBatchqueryModel()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'position_ids' in d:
            o.position_ids = d['position_ids']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


