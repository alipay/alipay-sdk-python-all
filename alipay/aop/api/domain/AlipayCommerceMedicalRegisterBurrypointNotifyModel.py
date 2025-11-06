#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterBurrypointNotifyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._burry_point_error_msg = None
        self._burry_point_type = None
        self._burrypoint_prop = None
        self._channel = None
        self._isv_code = None
        self._isv_doc_name = None
        self._isv_doc_no = None
        self._isv_hos_dept_name = None
        self._isv_hos_dept_no = None
        self._isv_hos_name = None
        self._isv_hos_no = None
        self._number_id = None
        self._open_id = None
        self._order_prop = None
        self._platform_code = None
        self._register_date = None
        self._register_id = None
        self._request_id = None
        self._scene_code = None
        self._sub_scene_code = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def burry_point_error_msg(self):
        return self._burry_point_error_msg

    @burry_point_error_msg.setter
    def burry_point_error_msg(self, value):
        self._burry_point_error_msg = value
    @property
    def burry_point_type(self):
        return self._burry_point_type

    @burry_point_type.setter
    def burry_point_type(self, value):
        self._burry_point_type = value
    @property
    def burrypoint_prop(self):
        return self._burrypoint_prop

    @burrypoint_prop.setter
    def burrypoint_prop(self, value):
        self._burrypoint_prop = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def isv_doc_name(self):
        return self._isv_doc_name

    @isv_doc_name.setter
    def isv_doc_name(self, value):
        self._isv_doc_name = value
    @property
    def isv_doc_no(self):
        return self._isv_doc_no

    @isv_doc_no.setter
    def isv_doc_no(self, value):
        self._isv_doc_no = value
    @property
    def isv_hos_dept_name(self):
        return self._isv_hos_dept_name

    @isv_hos_dept_name.setter
    def isv_hos_dept_name(self, value):
        self._isv_hos_dept_name = value
    @property
    def isv_hos_dept_no(self):
        return self._isv_hos_dept_no

    @isv_hos_dept_no.setter
    def isv_hos_dept_no(self, value):
        self._isv_hos_dept_no = value
    @property
    def isv_hos_name(self):
        return self._isv_hos_name

    @isv_hos_name.setter
    def isv_hos_name(self, value):
        self._isv_hos_name = value
    @property
    def isv_hos_no(self):
        return self._isv_hos_no

    @isv_hos_no.setter
    def isv_hos_no(self, value):
        self._isv_hos_no = value
    @property
    def number_id(self):
        return self._number_id

    @number_id.setter
    def number_id(self, value):
        self._number_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_prop(self):
        return self._order_prop

    @order_prop.setter
    def order_prop(self, value):
        self._order_prop = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sub_scene_code(self):
        return self._sub_scene_code

    @sub_scene_code.setter
    def sub_scene_code(self, value):
        self._sub_scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.burry_point_error_msg:
            if hasattr(self.burry_point_error_msg, 'to_alipay_dict'):
                params['burry_point_error_msg'] = self.burry_point_error_msg.to_alipay_dict()
            else:
                params['burry_point_error_msg'] = self.burry_point_error_msg
        if self.burry_point_type:
            if hasattr(self.burry_point_type, 'to_alipay_dict'):
                params['burry_point_type'] = self.burry_point_type.to_alipay_dict()
            else:
                params['burry_point_type'] = self.burry_point_type
        if self.burrypoint_prop:
            if hasattr(self.burrypoint_prop, 'to_alipay_dict'):
                params['burrypoint_prop'] = self.burrypoint_prop.to_alipay_dict()
            else:
                params['burrypoint_prop'] = self.burrypoint_prop
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.isv_doc_name:
            if hasattr(self.isv_doc_name, 'to_alipay_dict'):
                params['isv_doc_name'] = self.isv_doc_name.to_alipay_dict()
            else:
                params['isv_doc_name'] = self.isv_doc_name
        if self.isv_doc_no:
            if hasattr(self.isv_doc_no, 'to_alipay_dict'):
                params['isv_doc_no'] = self.isv_doc_no.to_alipay_dict()
            else:
                params['isv_doc_no'] = self.isv_doc_no
        if self.isv_hos_dept_name:
            if hasattr(self.isv_hos_dept_name, 'to_alipay_dict'):
                params['isv_hos_dept_name'] = self.isv_hos_dept_name.to_alipay_dict()
            else:
                params['isv_hos_dept_name'] = self.isv_hos_dept_name
        if self.isv_hos_dept_no:
            if hasattr(self.isv_hos_dept_no, 'to_alipay_dict'):
                params['isv_hos_dept_no'] = self.isv_hos_dept_no.to_alipay_dict()
            else:
                params['isv_hos_dept_no'] = self.isv_hos_dept_no
        if self.isv_hos_name:
            if hasattr(self.isv_hos_name, 'to_alipay_dict'):
                params['isv_hos_name'] = self.isv_hos_name.to_alipay_dict()
            else:
                params['isv_hos_name'] = self.isv_hos_name
        if self.isv_hos_no:
            if hasattr(self.isv_hos_no, 'to_alipay_dict'):
                params['isv_hos_no'] = self.isv_hos_no.to_alipay_dict()
            else:
                params['isv_hos_no'] = self.isv_hos_no
        if self.number_id:
            if hasattr(self.number_id, 'to_alipay_dict'):
                params['number_id'] = self.number_id.to_alipay_dict()
            else:
                params['number_id'] = self.number_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_prop:
            if hasattr(self.order_prop, 'to_alipay_dict'):
                params['order_prop'] = self.order_prop.to_alipay_dict()
            else:
                params['order_prop'] = self.order_prop
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sub_scene_code:
            if hasattr(self.sub_scene_code, 'to_alipay_dict'):
                params['sub_scene_code'] = self.sub_scene_code.to_alipay_dict()
            else:
                params['sub_scene_code'] = self.sub_scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterBurrypointNotifyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'burry_point_error_msg' in d:
            o.burry_point_error_msg = d['burry_point_error_msg']
        if 'burry_point_type' in d:
            o.burry_point_type = d['burry_point_type']
        if 'burrypoint_prop' in d:
            o.burrypoint_prop = d['burrypoint_prop']
        if 'channel' in d:
            o.channel = d['channel']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'isv_doc_name' in d:
            o.isv_doc_name = d['isv_doc_name']
        if 'isv_doc_no' in d:
            o.isv_doc_no = d['isv_doc_no']
        if 'isv_hos_dept_name' in d:
            o.isv_hos_dept_name = d['isv_hos_dept_name']
        if 'isv_hos_dept_no' in d:
            o.isv_hos_dept_no = d['isv_hos_dept_no']
        if 'isv_hos_name' in d:
            o.isv_hos_name = d['isv_hos_name']
        if 'isv_hos_no' in d:
            o.isv_hos_no = d['isv_hos_no']
        if 'number_id' in d:
            o.number_id = d['number_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_prop' in d:
            o.order_prop = d['order_prop']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'register_id' in d:
            o.register_id = d['register_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sub_scene_code' in d:
            o.sub_scene_code = d['sub_scene_code']
        return o


