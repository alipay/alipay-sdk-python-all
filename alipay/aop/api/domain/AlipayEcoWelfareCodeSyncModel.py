#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WelfareEcoStoreInfo import WelfareEcoStoreInfo


class AlipayEcoWelfareCodeSyncModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._code = None
        self._code_expire_date = None
        self._code_num = None
        self._code_pic_url = None
        self._code_start_date = None
        self._code_status = None
        self._code_status_date = None
        self._code_type = None
        self._extend_params = None
        self._isv_code = None
        self._store_info = None
        self._sync_date = None
        self._welfare_user_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def code_expire_date(self):
        return self._code_expire_date

    @code_expire_date.setter
    def code_expire_date(self, value):
        self._code_expire_date = value
    @property
    def code_num(self):
        return self._code_num

    @code_num.setter
    def code_num(self, value):
        self._code_num = value
    @property
    def code_pic_url(self):
        return self._code_pic_url

    @code_pic_url.setter
    def code_pic_url(self, value):
        self._code_pic_url = value
    @property
    def code_start_date(self):
        return self._code_start_date

    @code_start_date.setter
    def code_start_date(self, value):
        self._code_start_date = value
    @property
    def code_status(self):
        return self._code_status

    @code_status.setter
    def code_status(self, value):
        self._code_status = value
    @property
    def code_status_date(self):
        return self._code_status_date

    @code_status_date.setter
    def code_status_date(self, value):
        self._code_status_date = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def store_info(self):
        return self._store_info

    @store_info.setter
    def store_info(self, value):
        if isinstance(value, WelfareEcoStoreInfo):
            self._store_info = value
        else:
            self._store_info = WelfareEcoStoreInfo.from_alipay_dict(value)
    @property
    def sync_date(self):
        return self._sync_date

    @sync_date.setter
    def sync_date(self, value):
        self._sync_date = value
    @property
    def welfare_user_id(self):
        return self._welfare_user_id

    @welfare_user_id.setter
    def welfare_user_id(self, value):
        self._welfare_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.code_expire_date:
            if hasattr(self.code_expire_date, 'to_alipay_dict'):
                params['code_expire_date'] = self.code_expire_date.to_alipay_dict()
            else:
                params['code_expire_date'] = self.code_expire_date
        if self.code_num:
            if hasattr(self.code_num, 'to_alipay_dict'):
                params['code_num'] = self.code_num.to_alipay_dict()
            else:
                params['code_num'] = self.code_num
        if self.code_pic_url:
            if hasattr(self.code_pic_url, 'to_alipay_dict'):
                params['code_pic_url'] = self.code_pic_url.to_alipay_dict()
            else:
                params['code_pic_url'] = self.code_pic_url
        if self.code_start_date:
            if hasattr(self.code_start_date, 'to_alipay_dict'):
                params['code_start_date'] = self.code_start_date.to_alipay_dict()
            else:
                params['code_start_date'] = self.code_start_date
        if self.code_status:
            if hasattr(self.code_status, 'to_alipay_dict'):
                params['code_status'] = self.code_status.to_alipay_dict()
            else:
                params['code_status'] = self.code_status
        if self.code_status_date:
            if hasattr(self.code_status_date, 'to_alipay_dict'):
                params['code_status_date'] = self.code_status_date.to_alipay_dict()
            else:
                params['code_status_date'] = self.code_status_date
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.store_info:
            if hasattr(self.store_info, 'to_alipay_dict'):
                params['store_info'] = self.store_info.to_alipay_dict()
            else:
                params['store_info'] = self.store_info
        if self.sync_date:
            if hasattr(self.sync_date, 'to_alipay_dict'):
                params['sync_date'] = self.sync_date.to_alipay_dict()
            else:
                params['sync_date'] = self.sync_date
        if self.welfare_user_id:
            if hasattr(self.welfare_user_id, 'to_alipay_dict'):
                params['welfare_user_id'] = self.welfare_user_id.to_alipay_dict()
            else:
                params['welfare_user_id'] = self.welfare_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoWelfareCodeSyncModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'code' in d:
            o.code = d['code']
        if 'code_expire_date' in d:
            o.code_expire_date = d['code_expire_date']
        if 'code_num' in d:
            o.code_num = d['code_num']
        if 'code_pic_url' in d:
            o.code_pic_url = d['code_pic_url']
        if 'code_start_date' in d:
            o.code_start_date = d['code_start_date']
        if 'code_status' in d:
            o.code_status = d['code_status']
        if 'code_status_date' in d:
            o.code_status_date = d['code_status_date']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'store_info' in d:
            o.store_info = d['store_info']
        if 'sync_date' in d:
            o.sync_date = d['sync_date']
        if 'welfare_user_id' in d:
            o.welfare_user_id = d['welfare_user_id']
        return o


