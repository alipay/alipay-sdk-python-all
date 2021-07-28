#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneKidsCloseModel(object):

    def __init__(self):
        self._biz_code = None
        self._ext_info = None
        self._invoke_id = None
        self._memo = None
        self._parent_uid = None
        self._school_stdcode = None
        self._sub_biz_code = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def invoke_id(self):
        return self._invoke_id

    @invoke_id.setter
    def invoke_id(self, value):
        self._invoke_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def parent_uid(self):
        return self._parent_uid

    @parent_uid.setter
    def parent_uid(self, value):
        self._parent_uid = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def sub_biz_code(self):
        return self._sub_biz_code

    @sub_biz_code.setter
    def sub_biz_code(self, value):
        self._sub_biz_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.invoke_id:
            if hasattr(self.invoke_id, 'to_alipay_dict'):
                params['invoke_id'] = self.invoke_id.to_alipay_dict()
            else:
                params['invoke_id'] = self.invoke_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.parent_uid:
            if hasattr(self.parent_uid, 'to_alipay_dict'):
                params['parent_uid'] = self.parent_uid.to_alipay_dict()
            else:
                params['parent_uid'] = self.parent_uid
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        if self.sub_biz_code:
            if hasattr(self.sub_biz_code, 'to_alipay_dict'):
                params['sub_biz_code'] = self.sub_biz_code.to_alipay_dict()
            else:
                params['sub_biz_code'] = self.sub_biz_code
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
        o = AlipayCommerceEducateSceneKidsCloseModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'invoke_id' in d:
            o.invoke_id = d['invoke_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'parent_uid' in d:
            o.parent_uid = d['parent_uid']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'sub_biz_code' in d:
            o.sub_biz_code = d['sub_biz_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


