#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BuyerInfo import BuyerInfo
from alipay.aop.api.domain.HomeNormalApiContent import HomeNormalApiContent


class AlipayIserviceItaskMerchantRecordSyncModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_id = None
        self._buyer_id = None
        self._buyer_info = None
        self._content = None
        self._is_alipay_user = None
        self._is_authorize = None
        self._msg_time = None
        self._node_code = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, BuyerInfo):
            self._buyer_info = value
        else:
            self._buyer_info = BuyerInfo.from_alipay_dict(value)
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, HomeNormalApiContent):
            self._content = value
        else:
            self._content = HomeNormalApiContent.from_alipay_dict(value)
    @property
    def is_alipay_user(self):
        return self._is_alipay_user

    @is_alipay_user.setter
    def is_alipay_user(self, value):
        self._is_alipay_user = value
    @property
    def is_authorize(self):
        return self._is_authorize

    @is_authorize.setter
    def is_authorize(self, value):
        self._is_authorize = value
    @property
    def msg_time(self):
        return self._msg_time

    @msg_time.setter
    def msg_time(self, value):
        self._msg_time = value
    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.is_alipay_user:
            if hasattr(self.is_alipay_user, 'to_alipay_dict'):
                params['is_alipay_user'] = self.is_alipay_user.to_alipay_dict()
            else:
                params['is_alipay_user'] = self.is_alipay_user
        if self.is_authorize:
            if hasattr(self.is_authorize, 'to_alipay_dict'):
                params['is_authorize'] = self.is_authorize.to_alipay_dict()
            else:
                params['is_authorize'] = self.is_authorize
        if self.msg_time:
            if hasattr(self.msg_time, 'to_alipay_dict'):
                params['msg_time'] = self.msg_time.to_alipay_dict()
            else:
                params['msg_time'] = self.msg_time
        if self.node_code:
            if hasattr(self.node_code, 'to_alipay_dict'):
                params['node_code'] = self.node_code.to_alipay_dict()
            else:
                params['node_code'] = self.node_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskMerchantRecordSyncModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'content' in d:
            o.content = d['content']
        if 'is_alipay_user' in d:
            o.is_alipay_user = d['is_alipay_user']
        if 'is_authorize' in d:
            o.is_authorize = d['is_authorize']
        if 'msg_time' in d:
            o.msg_time = d['msg_time']
        if 'node_code' in d:
            o.node_code = d['node_code']
        return o


