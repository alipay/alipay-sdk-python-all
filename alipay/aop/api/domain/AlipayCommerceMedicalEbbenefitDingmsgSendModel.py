#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RemindVO import RemindVO


class AlipayCommerceMedicalEbbenefitDingmsgSendModel(object):

    def __init__(self):
        self._biz_type = None
        self._data = None
        self._eb_user_id = None
        self._inquiry_mode = None
        self._jump_url = None
        self._msg_time = None
        self._msg_type = None
        self._order_id = None
        self._order_type = None
        self._out_order_id = None
        self._out_parent_order_id = None
        self._out_sub_user_id = None
        self._out_user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, RemindVO):
            self._data = value
        else:
            self._data = RemindVO.from_alipay_dict(value)
    @property
    def eb_user_id(self):
        return self._eb_user_id

    @eb_user_id.setter
    def eb_user_id(self, value):
        self._eb_user_id = value
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def msg_time(self):
        return self._msg_time

    @msg_time.setter
    def msg_time(self, value):
        self._msg_time = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_parent_order_id(self):
        return self._out_parent_order_id

    @out_parent_order_id.setter
    def out_parent_order_id(self, value):
        self._out_parent_order_id = value
    @property
    def out_sub_user_id(self):
        return self._out_sub_user_id

    @out_sub_user_id.setter
    def out_sub_user_id(self, value):
        self._out_sub_user_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.eb_user_id:
            if hasattr(self.eb_user_id, 'to_alipay_dict'):
                params['eb_user_id'] = self.eb_user_id.to_alipay_dict()
            else:
                params['eb_user_id'] = self.eb_user_id
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.msg_time:
            if hasattr(self.msg_time, 'to_alipay_dict'):
                params['msg_time'] = self.msg_time.to_alipay_dict()
            else:
                params['msg_time'] = self.msg_time
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_parent_order_id:
            if hasattr(self.out_parent_order_id, 'to_alipay_dict'):
                params['out_parent_order_id'] = self.out_parent_order_id.to_alipay_dict()
            else:
                params['out_parent_order_id'] = self.out_parent_order_id
        if self.out_sub_user_id:
            if hasattr(self.out_sub_user_id, 'to_alipay_dict'):
                params['out_sub_user_id'] = self.out_sub_user_id.to_alipay_dict()
            else:
                params['out_sub_user_id'] = self.out_sub_user_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEbbenefitDingmsgSendModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'data' in d:
            o.data = d['data']
        if 'eb_user_id' in d:
            o.eb_user_id = d['eb_user_id']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'msg_time' in d:
            o.msg_time = d['msg_time']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_parent_order_id' in d:
            o.out_parent_order_id = d['out_parent_order_id']
        if 'out_sub_user_id' in d:
            o.out_sub_user_id = d['out_sub_user_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        return o


